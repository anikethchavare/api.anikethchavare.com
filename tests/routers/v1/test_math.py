# api.anikethchavare.com - tests/routers/v1/test_math.py

"""
Copyright 2026 Aniketh Chavare (anikethchavare@zohomail.in)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# Imports
import math
import pytest
from server import app
from fastapi.testclient import TestClient

# Initializing the TestClient
client = TestClient(app)

# Test Route 1: Main (app_v1_math)
def test_app_v1_math_main():
    """ Tests the base entry point of the math utility namespace. """

    response = client.get("/v1/math/")
    assert response.status_code == 200

    json_data = response.json()
    assert json_data["success"] is True
    assert "math" in json_data["message"]

# Test Route 2: Trigonometry (app_v1_math)
def test_app_v1_math_trigonometry():
    """ Tests the base entry point of the trigonometry sub-utility namespace. """

    response = client.get("/v1/math/trigonometry")
    assert response.status_code == 200

    json_data = response.json()
    assert json_data["success"] is True
    assert "trigonometry" in json_data["message"]

# Test Route 3: Trigonometry - Degrees to Radians (app_v1_math)
def test_app_v1_math_trigonometry_degrees_to_radians():
    """ Tests degree to radian conversions with both int and float inputs. """

    response = client.get("/v1/math/trigonometry/degrees-to-radians?degrees=180")
    assert response.status_code == 200
    assert response.json()["data"]["radians"] == math.pi

    response = client.get("/v1/math/trigonometry/degrees-to-radians?degrees=90.0")
    assert response.status_code == 200
    assert response.json()["data"]["radians"] == math.pi / 2
    assert client.get("/v1/math/trigonometry/degrees-to-radians").status_code == 422

# Test Route 4: Trigonometry - Radians to Degrees (app_v1_math)
def test_app_v1_math_trigonometry_radians_to_degrees():
    """ Tests radian to degree conversions with both int and float inputs. """

    response = client.get(f"/v1/math/trigonometry/radians-to-degrees?radians={math.pi}")
    assert response.status_code == 200
    assert response.json()["data"]["degrees"] == 180.0
    assert client.get("/v1/math/trigonometry/radians-to-degrees?radians=invalid").status_code == 422

# Test Route 5: Trigonometry - Trigonometric Function Evaluation Tests -> Success (app_v1_math)
@pytest.mark.parametrize("endpoint, val, unit, expected", [
    ("sin", 90, "degrees", 1.0),
    ("sin", math.pi / 2, "radians", 1.0),
    ("cos", 0, "degrees", 1.0),
    ("cos", 0.0, "radians", 1.0),
    ("tan", 45, "degrees", 1.0),
])
def test_app_v1_math_trigonometry_trigonometric_functions_success(endpoint, val, unit, expected):
    """ Parametrized verification of positive execution flows across base functions ."""

    response = client.get(f"/v1/math/trigonometry/{endpoint}?value={val}&unit={unit}")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert pytest.approx(response.json()["data"]["result"], rel=1e-5) == expected

# Test Route 6: Trigonometry - Trigonometric Function Evaluation Tests -> Invalid Unit (app_v1_math)
@pytest.mark.parametrize("endpoint", ["sin", "cos", "tan", "cosec", "sec", "cot"])
def test_app_v1_math_trigonometry_trigonometric_functions_invalid_unit(endpoint):
    """ Ensure Pydantic Literal type validations successfully intercept non-supported units. """

    response = client.get(f"/v1/math/trigonometry/{endpoint}?value=45&unit=invalid_unit")
    assert response.status_code == 422
    assert response.json()["success"] is False

# Test Route 7: Trigonometry - Trigonometric Reciprocal & Complex Exception Handling Boundaries -> Success (app_v1_math)
def test_app_v1_math_trigonometry_trigonometric_reciprocal_success():
    """ Verify standard operational flows for cosec, sec, and cot functions. """

    response_cosec = client.get("/v1/math/trigonometry/cosec?value=90&unit=degrees")
    assert response_cosec.status_code == 200
    assert pytest.approx(response_cosec.json()["data"]["result"]) == 1.0

    response_sec = client.get("/v1/math/trigonometry/sec?value=0&unit=degrees")
    assert response_sec.status_code == 200
    assert pytest.approx(response_sec.json()["data"]["result"]) == 1.0

    response_cot = client.get("/v1/math/trigonometry/cot?value=45&unit=degrees")
    assert response_cot.status_code == 200
    assert pytest.approx(response_cot.json()["data"]["result"]) == 1.0

# Test Route 8: Trigonometry - Trigonometric Reciprocal & Complex Exception Handling Boundaries -> Zero Division Exception (app_v1_math)
@pytest.mark.parametrize("endpoint, val, unit", [
    ("cosec", 0, "degrees"),
    ("cosec", 0.0, "radians"),
    ("cot", 0, "degrees"),
    ("cot", 0.0, "radians"),
])
def test_app_v1_math_trigonometry_trigonometric_zero_division_exception(endpoint, val, unit):
    """ Ensure literal ZeroDivisionError bounds return a structural 422 payload. """

    response = client.get(f"/v1/math/trigonometry/{endpoint}?value={val}&unit={unit}")
    assert response.status_code == 422

    json_data = response.json()
    assert json_data["success"] is False
    assert "division by zero" in json_data["message"].lower()

# Test Route 9: Statistics (app_v1_math)
def test_app_v1_math_statistics():
    """ Tests the base informational entry point of the statistics sub-utility namespace. """

    response = client.get("/v1/math/statistics")
    assert response.status_code == 200

    json_data = response.json()
    assert json_data["success"] is True
    assert "statistics" in json_data["message"]

# Test Routes 10: Statistics - Evaluation Tests -> Success & Min Length Validation (app_v1_math)
@pytest.mark.parametrize("endpoint, dataset, key, expected", [
    ("mean", [1, 2, 3, 4, 5], "mean", 3.0),
    ("mean", [10.5, 20.5], "mean", 15.5),
    ("median", [1, 3, 3, 6, 7, 8, 9], "median", 6.0),
    ("median", [1, 2, 3, 4], "median", 2.5),
    ("mode", [1, 2, 2, 3], "mode", [2]),
    ("mode", [1, 1, 2, 2, 3], "mode", [1, 2])
])
def test_app_v1_math_statistics_endpoints_success(endpoint, dataset, key, expected):
    """ Verifies correct calculation values across mean, median, and mode array handlers. """

    response = client.getClient().post(f"/v1/math/statistics/{endpoint}", json={"data": dataset}) if hasattr(client, "getClient") else client.post(f"/v1/math/statistics/{endpoint}", json={"data": dataset})
    assert response.status_code == 200

    json_data = response.json()
    assert json_data["success"] is True
    assert json_data["data"][key] == expected

@pytest.mark.parametrize("endpoint", ["mean", "median", "mode"])
def test_app_v1_math_statistics_min_length_validation(endpoint):
    """ Verifies that passing an empty list fails the min_length=1 guardrail. """

    response = client.post(f"/v1/math/statistics/{endpoint}", json={"data": []})
    assert response.status_code == 422
    assert response.json()["success"] is False

# Test Route 11: Algebra (app_v1_math)
def test_app_v1_math_algebra():
    """ Tests the base informational entry point of the algebra sub-utility namespace. """

    response = client.get("/v1/math/algebra")
    assert response.status_code == 200

    json_data = response.json()
    assert json_data["success"] is True
    assert "algebra" in json_data["message"]

# Test Route 12: Algebra - Constraints -> Leading Coefficient Cannot Be Zero (app_v1_math)
@pytest.mark.parametrize("endpoint", ["discriminant", "roots"])
def test_app_v1_math_algebra_leading_coefficient_zero(endpoint):
    """ Ensures requests are rejected with a 422 if the leading coefficient (a) is 0. """

    response = client.post(f"/v1/math/algebra/{endpoint}", json={"coefficients": [0, 2, 3]})
    assert response.status_code == 422
    assert "must not be zero" in response.json()["message"]

# Test Route 13: Algebra - Constraints -> Length Bounds Validation (app_v1_math)
@pytest.mark.parametrize("endpoint, payload", [
    ("discriminant", [1, 2]),
    ("discriminant", [1, 2, 3, 4, 5]),
    ("roots", [1, 2]),
    ("roots", [1, 2, 3, 4, 5])
])
def test_app_v1_math_algebra_length_constraints(endpoint, payload):
    """ Verifies that array length bounds (min_length=3, max_length=4) are strictly enforced. """

    response = client.post(f"/v1/math/algebra/{endpoint}", json={"coefficients": payload})
    assert response.status_code == 422

# Test Route 14: Algebra - Discriminant Execution Paths (app_v1_math)
def test_app_v1_math_algebra_discriminant_calculation():
    """ Verifies quadratic and cubic discriminant evaluations work correctly. """

    response_quad = client.post("/v1/math/algebra/discriminant", json={"coefficients": [1, 5, 6]})
    assert response_quad.status_code == 200
    assert response_quad.json()["data"]["discriminant"] == 1

    response_cubic = client.post("/v1/math/algebra/discriminant", json={"coefficients": [1, -6, 11, -6]})
    assert response_cubic.status_code == 200
    assert "discriminant" in response_cubic.json()["data"]

# Test Route 15: Algebra - Roots Processing Paths (app_v1_math)
def test_app_v1_math_algebra_roots_serialization():
    """ Ensures algebraic root calculation handles types and outputs cleanly without dropping payloads. """

    response_real = client.post("/v1/math/algebra/roots", json={"coefficients": [1, -5, 6]})
    assert response_real.status_code == 200

    roots_real = response_real.json()["data"]["roots"]
    assert len(roots_real) == 2
    assert pytest.approx(sorted(roots_real)) == [2.0, 3.0]

    response_complex = client.post("/v1/math/algebra/roots", json={"coefficients": [1, 0, 1]})
    assert response_complex.status_code == 200

    roots_complex = response_complex.json()["data"]["roots"]
    assert len(roots_complex) == 2
    assert any("j" in str(r) for r in roots_complex)