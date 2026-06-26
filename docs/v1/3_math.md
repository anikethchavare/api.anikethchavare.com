# api.anikethchavare.com / docs / v1 / 3_math.md

This document outlines the endpoints available under the `math` utility namespace.

<hr>

## 1. 📡 Endpoints

These endpoints are bound directly to the `app_v1_math` router and operate under the `/math` prefix namespace.

For faster navigation, select one of the following mathematical sub-utility namespaces to jump directly to its documentation:
* **[/trigonometry](#trigonometry)** — Converts degrees/radians and evaluates all standard and reciprocal trigonometric ratios.
* **[/statistics](#statistics)** — Computes metrics like mean, median, and multi-modal datasets.
* **[/algebra](#algebra)** — Calculates discriminants and isolates complex roots for equations.
* **[/arithmetic](#arithmetic)** — Handles prime checks, factorials, HCF, LCM, and sequential series generation.
* **[/complex](#complex)** — Extracts properties like modulus, conjugates, inverses, and polar forms.

### 1. `/v1/math`
* **Description:** Serves as the introductory entry point to the utility namespace.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * *Returns an empty dictionary `{}` inside the core `data` block.*
* **Query Parameters:** None
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:** None
* **Example Request URL:** `https://api.anikethchavare.com/v1/math`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Welcome to the 'math' utility namespace. Check the documentation for available endpoints.",
    "data": {},
    "meta": {
        "rate_limit": "60 requests per minute.",
        "help": "Check the API v1 documentation (/math) for available endpoints.",
        "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs/v1/3_math.md"
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-23T15:57:26.063993+00:00",
    "request_id": "req_8a3a84f9-b6e7-482e-abad-b4309a591488",
    "status_code": 200
}
```

### 2. <span id="trigonometry">`/v1/math/trigonometry`</span>
* **Description:** Serves as the introductory entry point to the sub-utility namespace.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * *Returns an empty dictionary `{}` inside the core `data` block.*
* **Query Parameters:** None
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:** None
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/trigonometry`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Welcome to the 'trigonometry' sub-utility namespace under 'math'. Check the documentation for available endpoints.",
    "data": {},
    "meta": {
        "rate_limit": "60 requests per minute.",
        "help": "Check the API v1 documentation (/math) for available endpoints.",
        "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs/v1/3_math.md"
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-23T15:57:26.063993+00:00",
    "request_id": "req_aa607abd-60f8-4ca9-a96b-b2ad2f51509c",
    "status_code": 200
}
```

### 3. `/v1/math/trigonometry/degrees-to-radians`
* **Description:** Converts degrees to radians.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `radians` *(Int/Float)*: The converted value i.e. radians.
* **Query Parameters:**
  * `degrees` *(Int/Float, Required)*: The value of degrees to convert to radians.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:** None
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/trigonometry/degrees-to-radians?degrees=10`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully converted degrees to radians.",
    "data": {
        "radians": 0.17453292519943
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-23T16:00:57.584318+00:00",
    "request_id": "req_7de72f6d-54c0-4846-9766-8a4229249235",
    "status_code": 200
}
```

### 4. `/v1/math/trigonometry/radians-to-degrees`
* **Description:** Converts radians to degrees.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `degrees` *(Int/Float)*: The converted value i.e. degrees.
* **Query Parameters:**
  * `radians` *(Int/Float, Required)*: The value of radians to convert to degrees.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:** None
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/trigonometry/radians-to-degrees?radians=10`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully converted radians to degrees.",
    "data": {
        "degrees": 572.957795130823
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-23T16:00:57.584318+00:00",
    "request_id": "req_f96f62e7-5830-4808-99d3-3038a402bdb4",
    "status_code": 200
}
```

### 5. `/v1/math/trigonometry/sin`
* **Description:** Calculates the trigonometric sine of a given numeric value.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `result` *(Float)*: The evaluated trigonometric calculation result.
* **Query Parameters:**
  * `value` *(Int/Float, Required)*: The numeric input coordinate.
  * `unit` *(String, Required)*: The unit specification. Accepted values: `degrees` or `radians`.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:** None
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/trigonometry/sin?value=90&unit=degrees`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully converted the value from degrees to sin.",
    "data": {
        "result": 1.0
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-23T16:00:57.584318+00:00",
    "request_id": "req_1afa5a44-7935-406f-82ef-c00306759073",
    "status_code": 200
}
```

### 6. `/v1/math/trigonometry/cos`
* **Description:** Calculates the trigonometric cosine of a given numeric value.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `result` *(Float)*: The evaluated trigonometric calculation result.
* **Query Parameters:**
  * `value` *(Int/Float, Required)*: The numeric input coordinate.
  * `unit` *(String, Required)*: The unit specification. Accepted values: `degrees` or `radians`.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:** None
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/trigonometry/cos?value=90&unit=degrees`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully converted the value from degrees to cos.",
    "data": {
        "result": 6.12323399573677e-17
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-23T16:00:57.584318+00:00",
    "request_id": "req_846b3bf5-040e-4896-923d-6d9b49738f06",
    "status_code": 200
}
```

### 7. `/v1/math/trigonometry/tan`
* **Description:** Calculates the trigonometric tangent of a given numeric value.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `result` *(Float)*: The evaluated trigonometric calculation result.
* **Query Parameters:**
  * `value` *(Int/Float, Required)*: The numeric input coordinate.
  * `unit` *(String, Required)*: The unit specification. Accepted values: `degrees` or `radians`.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:** None
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/trigonometry/tan?value=90&unit=degrees`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully converted the value from degrees to tan.",
    "data": {
        "result": 16331239353195370
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-23T16:00:57.584318+00:00",
    "request_id": "req_8afe5abc-8e69-463c-8483-a85622c340af",
    "status_code": 200
}
```

### 8. `/v1/math/trigonometry/cosec`
* **Description:** Calculates the trigonometric cosecant of a given numeric value.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `result` *(Float)*: The evaluated trigonometric calculation result.
* **Query Parameters:**
  * `value` *(Int/Float, Required)*: The numeric input coordinate.
  * `unit` *(String, Required)*: The unit specification. Accepted values: `degrees` or `radians`.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:**
  * `422 Unprocessable Entity`: Triggered if the computed inputs evaluate to a mathematical division by zero asymptote.
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/trigonometry/cosec?value=90&unit=degrees`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully converted the value from degrees to cosec.",
    "data": {
        "result": 1
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-23T16:00:57.584318+00:00",
    "request_id": "req_846b3bf5-040e-4896-923d-6d9b49738f06",
    "status_code": 200
}
```

### 9. `/v1/math/trigonometry/sec`
* **Description:** Calculates the trigonometric secant of a given numeric value.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `result` *(Float)*: The evaluated trigonometric calculation result.
* **Query Parameters:**
  * `value` *(Int/Float, Required)*: The numeric input coordinate.
  * `unit` *(String, Required)*: The unit specification. Accepted values: `degrees` or `radians`.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:** None
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/trigonometry/sec?value=90&unit=degrees`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully converted the value from degrees to sec.",
    "data": {
        "result": 16331239353195370
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-23T16:00:57.584318+00:00",
    "request_id": "req_98029aa1-49a7-4888-b0fa-362d6e86ca7a",
    "status_code": 200
}
```

### 10. `/v1/math/trigonometry/cot`
* **Description:** Calculates the trigonometric cotangent of a given numeric value.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `result` *(Float)*: The evaluated trigonometric calculation result.
* **Query Parameters:**
  * `value` *(Int/Float, Required)*: The numeric input coordinate.
  * `unit` *(String, Required)*: The unit specification. Accepted values: `degrees` or `radians`.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:**
  * `422 Unprocessable Entity`: Triggered if the computed inputs evaluate to a mathematical division by zero asymptote.
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/trigonometry/cot?value=90&unit=degrees`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully converted the value from degrees to cot.",
    "data": {
        "result": 6.12323399573677e-17
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-23T16:00:57.584318+00:00",
    "request_id": "req_e185acaa-f0bd-414b-b605-c257ec92f475",
    "status_code": 200
}
```

### 11. <span id="statistics">`/v1/math/statistics`</span>
* **Description:** Serves as the introductory entry point to the sub-utility namespace.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * *Returns an empty dictionary `{}` inside the core `data` block.*
* **Query Parameters:** None
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:** None
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/statistics`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Welcome to the 'statistics' sub-utility namespace under 'math'. Check the documentation for available endpoints.",
    "data": {},
    "meta": {
        "rate_limit": "60 requests per minute.",
        "help": "Check the API v1 documentation (/math) for available endpoints.",
        "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs/v1/3_math.md"
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-24T07:10:00.777000+00:00",
    "request_id": "req_97d1710e-b2eb-4779-9b4f-f772f4f91676",
    "status_code": 200
}
```

### 12. `/v1/math/statistics/mean`
* **Description:** Calculates the mean (average) of the given values.
* **HTTP Method:** `POST`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `mean` *(Number)*: The calculated mean.
* **Query Parameters:** None
* **Headers Required:** None
* **Request Body Parameters (application/json):**
  * `data` *(List[Int/Float], Required)*: The list of values used to calculate the mean.
* **Custom Rate Limit:** None
* **Possible Local Exceptions:** None
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/statistics/mean`
* **Example Request Headers:** None
* **Example Request Body:**
```json
{
    "data": [1, 2, 3]
}
```
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully calculated the mean of the data.",
    "data": {
        "mean": 2
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-24T07:11:13.194478+00:00",
    "request_id": "req_462b6517-d58f-4c72-aad1-73cefb0dd0e4",
    "status_code": 200
}
```

### 13. `/v1/math/statistics/median`
* **Description:** Calculates the median of the given values.
* **HTTP Method:** `POST`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `median` *(Nummber)*: The calculated median.
* **Query Parameters:** None
* **Headers Required:** None
* **Request Body Parameters (application/json):**
  * `data` *(List[Int/Float], Required)*: The list of values used to calculate the median.
* **Custom Rate Limit:** None
* **Possible Local Exceptions:** None
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/statistics/median`
* **Example Request Headers:** None
* **Example Request Body:**
```json
{
    "data": [1, 2, 3]
}
```
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully calculated the median of the data.",
    "data": {
        "median": 2
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-24T07:13:03.626481+00:00",
    "request_id": "req_2d60a452-617d-47cf-bbde-dbd74bcbbf75",
    "status_code": 200
}
```

### 14. `/v1/math/statistics/mode`
* **Description:** Calculates the mode of the given values.
* **HTTP Method:** `POST`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `mode` *(List[Int/Float])*: The calculated mode(s).
* **Query Parameters:** None
* **Headers Required:** None
* **Request Body Parameters (application/json):**
  * `data` *(List[Int/Float], Required)*: The list of values used to calculate the mode.
* **Custom Rate Limit:** None
* **Possible Local Exceptions:** None
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/statistics/mode`
* **Example Request Headers:** None
* **Example Request Body:**
```json
{
    "data": [1, 2, 2, 3]
}
```
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully calculated the mode of the data.",
    "data": {
        "mode": [2]
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-24T07:13:44.795929+00:00",
    "request_id": "req_8634f107-0dbf-4c80-87bd-c3a6b91178ed",
    "status_code": 200
}
```

### 15. <span id="algebra">`/v1/math/algebra`</span>
* **Description:** Serves as the introductory entry point to the sub-utility namespace.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * *Returns an empty dictionary `{}` inside the core `data` block.*
* **Query Parameters:** None
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:** None
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/algebra`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Welcome to the 'algebra' sub-utility namespace under 'math'. Check the documentation for available endpoints.",
    "data": {},
    "meta": {
        "rate_limit": "60 requests per minute.",
        "help": "Check the API v1 documentation (/math) for available endpoints.",
        "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs/v1/3_math.md"
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-24T07:16:01.463254+00:00",
    "request_id": "req_81e9f432-a20c-4983-9065-cd4aae690901",
    "status_code": 200
}
```

### 16. `/v1/math/algebra/discriminant`
* **Description:** Calculates the discriminant of a quadratic or cubic equation.
* **HTTP Method:** `POST`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `discriminant` *(Int/Float)*: The evaluated mathematical discriminant.
* **Query Parameters:** None
* **Headers Required:** None
* **Request Body Parameters (application/json):**
  * `coefficients` *(List[Int/Float], Required)*: Explicit sequence array of length 3 (quadratic) or length 4 (cubic).
* **Custom Rate Limit:** None
* **Possible Local Exceptions:**
  * `422 Unprocessable Entity`: Triggered locally if the leading array term (`a`) equals 0. 
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/algebra/discriminant`
* **Example Request Headers:** None
* **Example Request Body:**
```json
{
    "coefficients": [1, 5, 6]
}
```
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully calculated the discriminant of the quadratic equation.",
    "data": {
        "discriminant": 1
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-24T07:20:14.218185+00:00",
    "request_id": "req_b423c818-3b05-4331-b3ac-2b0f72a42344",
    "status_code": 200
}
```

### 17. `/v1/math/algebra/roots`
* **Description:** Extracts all real and complex roots from quadratic or cubic systems.
* **HTTP Method:** `POST`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `roots` *(List[Int/Float])*: An ordered list containing evaluated roots. Complex numbers are safely cast as strings.
* **Query Parameters:** None
* **Headers Required:** None
* **Request Body Parameters (application/json):**
  * `coefficients` *(List[Int/Float], Required)*: Explicit sequence array of length 3 (quadratic) or length 4 (cubic).
* **Custom Rate Limit:** None
* **Possible Local Exceptions:**
  * `422 Unprocessable Entity`: Triggered locally if the leading array term (`a`) equals 0. 
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/algebra/roots`
* **Example Request Headers:** None
* **Example Request Body:**
```json
{
    "coefficients": [1, -5, 6]
}
```
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully calculated the roots of the quadratic equation.",
    "data": {
        "roots": [3.0000000000000004, 1.9999999999999998]
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-24T07:22:16.951173+00:00",
    "request_id": "req_86347ea8-c2ee-40fd-aa31-6ac7f596abfe",
    "status_code": 200
}
```

### 18. <span id="arithmetic">`/v1/math/arithmetic`</span>
* **Description:** Serves as the introductory entry point to the sub-utility namespace.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  *  *Returns an empty dictionary `{}` inside the core `data` block.*
* **Query Parameters:** None
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:** None
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/arithmetic`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Welcome to the 'arithmetic' sub-utility namespace under 'math'. Check the documentation for available endpoints.",
    "data": {},
    "meta": {
        "rate_limit": "60 requests per minute.",
        "help": "Check the API v1 documentation (/math) for available endpoints.",
        "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs/v1/3_math.md"
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-24T07:22:16.951173+00:00",
    "request_id": "req_a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5d6",
    "status_code": 200
}
```

### 19. `/v1/math/arithmetic/factorial`
* **Description:** Computes the mathematical factorial sequence calculation wrapper for any non-negative integer.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `factorial` *(Integer)*: The evaluated factorial value.
* **Query Parameters:**
  * `n` *(StrictInt, Required)*: The non-negative integer used to compute the factorial.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:**
  * `422 Unprocessable Entity` (`ValidationError`): Dispatched if `n` is omitted, not a strict integer, or evaluates to less than 0.
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/arithmetic/factorial?n=5`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully calculated the factorial.",
    "data": {
        "factorial": 120
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-26T12:01:00.000000+00:00",
    "request_id": "req_b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e",
    "status_code": 200
}
```

### 20. `/v1/math/arithmetic/is-prime`
* **Description:** Evaluates an integer input greater than or equal to 2 for mathematical primality.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `is_prime` *(Boolean)*: Evaluated truth value indicating primality.
* **Query Parameters:**
  * `n` *(StrictInt, Required)*: The target integer to evaluate for primality. The value must be greater than or equal to 2.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:**
  * `422 Unprocessable Entity` (`ValidationError`): Dispatched if `n` is less than 2.
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/arithmetic/is-prime?n=11`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully tested the number for primality.",
    "data": {
        "is_prime": true
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-26T12:01:00.000000+00:00",
    "request_id": "req_c3d4e5f6-a7b8-9c0d-1e2f-3a4b5c6d7e8f",
    "status_code": 200
}
```

### 21. `/v1/math/arithmetic/is-even`
* **Description:** Tests any arbitrary signed integer to determine if it evaluates to even parity.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `is_even` *(Boolean)*: Returns `true` if the value is even, otherwise `false`.
* **Query Parameters:**
  * `n` *(StrictInt, Required)*: The target integer to evaluate for even parity.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:**
  * `422 Unprocessable Entity` (`ValidationError`): Dispatched if `n` is omitted or is an invalid integer type.
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/arithmetic/is-even?n=42`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully tested the number for even parity.",
    "data": {
        "is_even": true
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-26T12:01:00.000000+00:00",
    "request_id": "req_d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a",
    "status_code": 200
}
```

### 22. `/v1/math/arithmetic/is-odd`
* **Description:** Tests any arbitrary signed integer to determine if it evaluates to odd parity.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `is_odd` *(Boolean)*: Returns `true` if the value is odd, otherwise `false`.
* **Query Parameters:**
  * `n` *(StrictInt, Required)*: The target integer to evaluate for odd parity.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:**
  * `422 Unprocessable Entity` (`ValidationError`): Dispatched if `n` is omitted or is an invalid integer type.
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/arithmetic/is-odd?n=13`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully tested the number for odd parity.",
    "data": {
        "is_odd": true
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-26T12:01:00.000000+00:00",
    "request_id": "req_e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b",
    "status_code": 200
}
```

### 23. `/v1/math/arithmetic/hcf`
* **Description:** Computes the Highest Common Factor (Greatest Common Divisor) across an array collection of integer values.
* **HTTP Method:** `POST`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `hcf` *(Integer)*: The calculated HCF value.
* **Query Parameters:** None
* **Headers Required:** None
* **Request Body Parameters (application/json):**
  * `data` *(List[Integer], Required)*: The list of numbers to compute the highest common factor for. The array must contain at least 1 element.
* **Custom Rate Limit:** None
* **Possible Local Exceptions:**
  * `422 Unprocessable Entity` (`ValidationError`): Dispatched if the array payload is missing or empty (`min_length=1`).
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/arithmetic/hcf`
* **Example Request Headers:** None
* **Example Request Body:**
```json
{
    "data": [12, 18, 24]
}
```
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully calculated the HCF of the given values.",
    "data": {
        "hcf": 6
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-26T12:01:00.000000+00:00",
    "request_id": "req_f6a7b8c9-d0e1-2f3a-4b5c-6d7e8f9a0b1c",
    "status_code": 200
}
```

### 24. `/v1/math/arithmetic/lcm`
* **Description:** Computes the Lowest Common Multiple across an array collection of integer values.
* **HTTP Method:** `POST`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `lcm` *(Integer)*: The calculated LCM value.
* **Query Parameters:** None
* **Headers Required:** None
* **Request Body Parameters (application/json):**
  * `data` *(List[Integer], Required)*: The list of numbers to compute the lowest common multiple for. The array must contain at least 1 element.
* **Custom Rate Limit:** None
* **Possible Local Exceptions:**
  * `422 Unprocessable Entity` (`ValidationError`): Dispatched if the array payload is missing or empty (`min_length=1`).
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/arithmetic/lcm`
* **Example Request Headers:** None
* **Example Request Body:**
```json
{
    "data": [12, 18, 24]
}
```
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully calculated the LCM of the given values.",
    "data": {
        "lcm": 72
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-26T12:01:00.000000+00:00",
    "request_id": "req_a7b8c9d0-e1f2-3a4b-5c6d-7e8f9a0b1c2d",
    "status_code": 200
}
```

### 25. `/v1/math/arithmetic/fibonacci`
* **Description:** Generates an ordered sequential array slice containing n elements matching the Fibonacci sequence matrix parameters.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `fibonacci_series` *(List[Integer])*: Array containing the generated sequence.
* **Query Parameters:**
  * `n` *(StrictInt, Required)*: The total number of terms to generate in the sequence. The value must be greater than or equal to 1.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:**
  * `422 Unprocessable Entity` (`ValidationError`): Dispatched if `n` evaluates to less than 1.
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/arithmetic/fibonacci?n=5`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully generated the Fibonacci sequence.",
    "data": {
        "fibonacci_series": [0, 1, 1, 2, 3]
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-26T12:01:00.000000+00:00",
    "request_id": "req_b8c9d0e1-f2a3-4b5c-6d7e-8f9a0b1c2d3e",
    "status_code": 200
}
```

### 26. <span id="complex">`/v1/math/complex`</span>
* **Description:** Serves as the introductory entry point to the sub-utility namespace.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * *Returns an empty dictionary `{}` inside the core `data` block.*
* **Query Parameters:** None
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:** None
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/complex`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Welcome to the 'complex' sub-utility namespace under 'math'. Check the documentation for available endpoints.",
    "data": {},
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-26T12:01:00.000000+00:00",
    "request_id": "req_c1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5d6",
    "status_code": 200
}
```

### 27. `/v1/math/complex/modulus`
* **Description:** Calculates the modulus (absolute value) of a given complex number.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `modulus` *(Float)*: The evaluated absolute magnitude of the complex number.
* **Query Parameters:**
  * `real` *(Float, Required)*: The real component of the complex number.
  * `imaginary` *(Float, Required)*: The imaginary component of the complex number.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:** None
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/complex/modulus?real=3&imaginary=4`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully calculated the modulus of the complex number.",
    "data": {
        "modulus": 5.0
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-26T12:01:00.000000+00:00",
    "request_id": "req_m1o2d3u4-l5u6-7s8b-9c0d-e1f2a3b4c5d6",
    "status_code": 200
}
```

### 28. `/v1/math/complex/conjugate`
* **Description:** Calculates the complex conjugate of a given complex number by reversing the sign of its imaginary part.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `conjugate` *(String)*: The string representation of the evaluated complex conjugate.
* **Query Parameters:**
  * `real` *(Float, Required)*: The real component of the complex number.
  * `imaginary` *(Float, Required)*: The imaginary component of the complex number.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:** None
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/complex/conjugate?real=2&imaginary=3`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully calculated the conjugate of the complex number.",
    "data": {
        "conjugate": "(2-3j)"
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-26T12:01:00.000000+00:00",
    "request_id": "req_c1o2n3j4-u5g6-7a8t-9c0d-e1f2a3b4c5d6",
    "status_code": 200
}
```

### 29. `/v1/math/complex/multiplicative-inverse`
* **Description:** Calculates the multiplicative inverse (reciprocal) of a given non-zero complex number.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `multiplicative_inverse` *(String)*: The string representation of the evaluated complex reciprocal.
* **Query Parameters:**
  * `real` *(Float, Required)*: The real component of the complex number.
  * `imaginary` *(Float, Required)*: The imaginary component of the complex number.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:**
  * `422 Unprocessable Entity`: Triggered if both the real and imaginary components are provided as 0, as the multiplicative inverse of zero is mathematically undefined.
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/complex/multiplicative-inverse?real=1&imaginary=0`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully calculated the multiplicative inverse of the complex number.",
    "data": {
        "multiplicative_inverse": "(1-0j)"
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-26T12:01:00.000000+00:00",
    "request_id": "req_m1u2l3t4-i5n6-7v8e-9r0s-e1f2a3b4c5d6",
    "status_code": 200
}
```

### 30. `/v1/math/complex/polar`
* **Description:** Converts a complex number from rectangular form (real and imaginary) to polar form coordinates (modulus $r$ and phase angle $\phi$).
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `polar_coordinates` *(List[Float])*: An array containing the modulus $r$ as the first element and the phase angle $\phi$ in radians as the second element.
* **Query Parameters:**
  * `real` *(Float, Required)*: The real component of the complex number.
  * `imaginary` *(Float, Required)*: The imaginary component of the complex number.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:** None
* **Example Request URL:** `https://api.anikethchavare.com/v1/math/complex/polar?real=1&imaginary=0`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully converted the complex number to polar form.",
    "data": {
        "polar_coordinates": [
            1.0,
            0.0
        ]
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-26T12:01:00.000000+00:00",
    "request_id": "req_p1o2l3a4-r5c6-7o8o-9r0d-e1f2a3b4c5d6",
    "status_code": 200
}
```

<hr>

## 2. 🧭 Next Guide

* **[4_entertainment.md](./4_entertainment.md) $\rightarrow$** Explore the `entertainment` utility namespace.

Additional feature sets, utility endpoints, and expanded business logic are currently in development and will be documented here as they release.