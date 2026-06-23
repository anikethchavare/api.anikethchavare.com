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

# Test Route 3: Degrees to Radians (app_v1_math)
def test_app_v1_math_degrees_to_radians():
    """ Tests degree to radian conversions with both int and float inputs. """

    response = client.get("/v1/math/trigonometry/degrees-to-radians?degrees=180")
    assert response.status_code == 200
    assert response.json()["data"]["radians"] == math.pi

    response = client.get("/v1/math/trigonometry/degrees-to-radians?degrees=90.0")
    assert response.status_code == 200
    assert response.json()["data"]["radians"] == math.pi / 2
    assert client.get("/v1/math/trigonometry/degrees-to-radians").status_code == 422

# Test Route 4: Radians to Degrees (app_v1_math)
def test_app_v1_math_radians_to_degrees():
    """ Tests radian to degree conversions with both int and float inputs. """

    response = client.get(f"/v1/math/trigonometry/radians-to-degrees?radians={math.pi}")
    assert response.status_code == 200
    assert response.json()["data"]["degrees"] == 180.0
    assert client.get("/v1/math/trigonometry/radians-to-degrees?radians=invalid").status_code == 422

# Test Route 5: Trigonometric Function Evaluation Tests -> Success (app_v1_math)
@pytest.mark.parametrize("endpoint, val, unit, expected", [
    ("sin", 90, "degrees", 1.0),
    ("sin", math.pi / 2, "radians", 1.0),
    ("cos", 0, "degrees", 1.0),
    ("cos", 0.0, "radians", 1.0),
    ("tan", 45, "degrees", 1.0),
])
def test_app_v1_math_trigonometric_functions_success(endpoint, val, unit, expected):
    """ Parametrized verification of positive execution flows across base functions ."""

    response = client.get(f"/v1/math/trigonometry/{endpoint}?value={val}&unit={unit}")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert pytest.approx(response.json()["data"]["result"], rel=1e-5) == expected

# Test Route 6: Trigonometric Function Evaluation Tests -> Invalid Unit (app_v1_math)
@pytest.mark.parametrize("endpoint", ["sin", "cos", "tan", "cosec", "sec", "cot"])
def test_app_v1_math_trigonometric_functions_invalid_unit(endpoint):
    """ Ensure Pydantic Literal type validations successfully intercept non-supported units. """

    response = client.get(f"/v1/math/trigonometry/{endpoint}?value=45&unit=invalid_unit")
    assert response.status_code == 422
    assert response.json()["success"] is False

# Test Route 7: Trigonometric Reciprocal & Complex Exception Handling Boundaries -> Success (app_v1_math)
def test_app_v1_math_trigonometric_reciprocal_success():
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

# Test Route 8: Trigonometric Reciprocal & Complex Exception Handling Boundaries -> Zero Division Exception (app_v1_math)
@pytest.mark.parametrize("endpoint, val, unit", [
    ("cosec", 0, "degrees"),
    ("cosec", 0.0, "radians"),
    ("cot", 0, "degrees"),
    ("cot", 0.0, "radians"),
])
def test_app_v1_math_trigonometric_zero_division_exception(endpoint, val, unit):
    """ Ensure literal ZeroDivisionError bounds return a structural 422 payload. """

    response = client.get(f"/v1/math/trigonometry/{endpoint}?value={val}&unit={unit}")
    assert response.status_code == 422

    json_data = response.json()
    assert json_data["success"] is False
    assert "division by zero" in json_data["message"].lower()