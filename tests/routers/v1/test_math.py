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

# Test Route 16: Arithmetic (app_v1_math)
def test_app_v1_math_arithmetic_main():
    """ Tests the entry point landing structure for the arithmetic namespace. """

    response = client.get("/v1/math/arithmetic")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "Welcome to the 'arithmetic' sub-utility namespace" in response.json()["message"]
    assert response.json()["data"] == {}

# Test Routes 17: Arithmetic - Factorial (app_v1_math)
def test_app_v1_math_arithmetic_factorial_success():
    """ Tests computing the factorial of a standard non-negative integer. """

    response = client.get("/v1/math/arithmetic/factorial?n=5")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["data"]["factorial"] == 120

def test_app_v1_math_arithmetic_factorial_zero_boundary():
    """ Tests computing the factorial of 0 (boundary case where 0! = 1). """

    response = client.get("/v1/math/arithmetic/factorial?n=0")
    assert response.status_code == 200
    assert response.json()["data"]["factorial"] == 1

def test_app_v1_math_arithmetic_factorial_negative_invalid():
    """ Tests that the system rejects negative integer bounds via Pydantic validator guards. """

    response = client.get("/v1/math/arithmetic/factorial?n=-5")
    assert response.status_code == 422
    assert response.json()["success"] is False
    assert "The request payload or parameters failed data validation checks." in response.json()["message"]

# Test Route 18: Arithmetic - Is Prime (app_v1_math)
def test_app_v1_math_arithmetic_is_prime_true():
    """ Tests verifying a known prime number. """

    response = client.get("/v1/math/arithmetic/is-prime?n=11")
    assert response.status_code == 200
    assert response.json()["data"]["is_prime"] is True

def test_app_v1_math_arithmetic_is_prime_false():
    """ Tests verifying a known composite number. """

    response = client.get("/v1/math/arithmetic/is-prime?n=4")
    assert response.status_code == 200
    assert response.json()["data"]["is_prime"] is False

def test_app_v1_math_arithmetic_is_prime_invalid_boundary():
    """ Tests that values less than 2 fail validation bounds. """

    response = client.get("/v1/math/arithmetic/is-prime?n=1")
    assert response.status_code == 422
    assert response.json()["success"] is False

# Test Route 19: Arithmetic - Is Even (app_v1_math)
def test_app_v1_math_arithmetic_is_even_true():
    """ Tests true and false conditions for even integer parity matching. """

    response_even = client.get("/v1/math/arithmetic/is-even?n=42")
    assert response_even.status_code == 200
    assert response_even.json()["data"]["is_even"] is True

    response_odd = client.get("/v1/math/arithmetic/is-even?n=13")
    assert response_odd.json()["data"]["is_even"] is False

# Test Route 20: Arithmetic - Is Odd (app_v1_math)
def test_app_v1_math_arithmetic_is_odd_true():
    """ Tests true and false conditions for odd integer parity matching. """

    response_odd = client.get("/v1/math/arithmetic/is-odd?n=13")
    assert response_odd.status_code == 200
    assert response_odd.json()["data"]["is_odd"] is True

    response_even = client.get("/v1/math/arithmetic/is-odd?n=42")
    assert response_even.json()["data"]["is_odd"] is False

# Test Routes 21: Arithmetic - HCF (app_v1_math)
def test_app_v1_math_arithmetic_hcf_success():
    """ Tests calculating the Highest Common Factor (GCD) of multiple numbers via POST payload. """

    payload = {"data": [12, 18, 24]}
    response = client.post("/v1/math/arithmetic/hcf", json=payload)
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["data"]["hcf"] == 6

def test_app_v1_math_arithmetic_hcf_empty_payload():
    """ Tests that empty arrays fail the min_length=1 schema verification step. """

    payload = {"data": []}
    response = client.post("/v1/math/arithmetic/hcf", json=payload)
    assert response.status_code == 422
    assert response.json()["success"] is False

# Test Route 22: Arithmetic - LCM (app_v1_math)
def test_app_v1_math_arithmetic_lcm_success():
    """ Tests calculating the Lowest Common Multiple of multiple numbers via POST payload. """

    payload = {"data": [12, 18, 24]}
    response = client.post("/v1/math/arithmetic/lcm", json=payload)
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["data"]["lcm"] == 72

# Test Route 23: Arithmetic - Fibonacci (app_v1_math)
def test_app_v1_math_arithmetic_fibonacci_sequence():
    """ Tests generating a multi-element sequence slice array. """

    response = client.get("/v1/math/arithmetic/fibonacci?n=5")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["data"]["fibonacci_series"] == [0, 1, 1, 2, 3]

def test_app_v1_math_arithmetic_fibonacci_bounds():
    """ Tests specific lower conditional sequences for n=1 and n=2 matching conditions. """

    res_one = client.get("/v1/math/arithmetic/fibonacci?n=1")
    assert res_one.json()["data"]["fibonacci_series"] == [0]

    res_two = client.get("/v1/math/arithmetic/fibonacci?n=2")
    assert res_two.json()["data"]["fibonacci_series"] == [0, 1]

def test_app_v1_math_arithmetic_fibonacci_invalid_bound():
    """ Tests validator fallback boundaries when passing zero counts (ge=1 rule violation). """

    response = client.get("/v1/math/arithmetic/fibonacci?n=0")
    assert response.status_code == 422
    assert response.json()["success"] is False

# Test Route 24: Complex (app_v1_math)
def test_app_v1_math_complex_main():
    """ Tests the entry point landing structure for the complex namespace. """

    response = client.get("/v1/math/complex")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "Welcome to the 'complex' sub-utility namespace" in response.json()["message"]
    assert response.json()["data"] == {}

# Test Route 25: Complex - Modulus (app_v1_math)
def test_app_v1_math_complex_modulus_success():
    """ Tests extracting the scalar modulus length using a standard 3-4-5 right triangle. """

    response = client.get("/v1/math/complex/modulus?real=3&imaginary=4")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["data"]["modulus"] == 5.0

# Test Route 26: Complex - Conjugate (app_v1_math)
def test_app_v1_math_complex_conjugate_success():
    """ Tests that the conjugate flips the sign of the imaginary component. """

    response = client.get("/v1/math/complex/conjugate?real=2&imaginary=3")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["data"]["conjugate"] == "(2-3j)"

# Test Routes 27: Complex - Multiplicative Inverse (app_v1_math)
def test_app_v1_math_complex_multiplicative_inverse_success():
    """ Tests calculating the multiplicative inverse of a valid non-zero complex number. """

    response = client.get("/v1/math/complex/multiplicative-inverse?real=1&imaginary=0")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["data"]["multiplicative_inverse"] == "(1-0j)"

def test_app_v1_math_complex_multiplicative_inverse_zero_boundary():
    """ Tests that passing zero values triggers your custom local 422 validation override. """

    response = client.get("/v1/math/complex/multiplicative-inverse?real=0&imaginary=0")
    assert response.status_code == 422
    assert response.json()["success"] is False
    assert "Multiplicative inverse of zero is undefined." in response.json()["message"]

# Test Route 28: Complex - Polar (app_v1_math)
def test_app_v1_math_complex_polar_success():
    """ Tests converting standard complex numbers to coordinate list polar form tuples. """

    response = client.get("/v1/math/complex/polar?real=1&imaginary=0")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert isinstance(response.json()["data"]["polar_coordinates"], list)
    assert response.json()["data"]["polar_coordinates"][0] == 1.0
    assert response.json()["data"]["polar_coordinates"][1] == 0.0