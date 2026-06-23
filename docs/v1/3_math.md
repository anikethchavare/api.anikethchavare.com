# api.anikethchavare.com / docs / v1 / 3_math.md

This document outlines the endpoints available under the `math` utility namespace.

<hr>

## 1. 📡 Endpoints

These endpoints are bound directly to the `app_v1_math` router and operate under the `/math` prefix namespace.

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

### 2. `/v1/math/trigonometry`
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
* **Possible Local Exceptions:**
  * `422 Unprocessable Entity`: Triggered if the computed inputs evaluate to a mathematical division by zero asymptote.
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
* **Possible Local Exceptions:**
  * `422 Unprocessable Entity`: Triggered if the computed inputs evaluate to a mathematical division by zero asymptote.
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

<hr>

## 2. 🧭 Next Guide

Additional feature sets, utility endpoints, and expanded business logic are currently in development and will be documented here as they release.