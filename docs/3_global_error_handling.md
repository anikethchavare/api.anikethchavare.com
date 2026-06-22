# api.anikethchavare.com / docs / 3_global_error_handling.md

This document serves as a comprehensive reference for the various global error types and HTTP exception states a client might encounter while interacting with the API. It details the structural format of failure responses and provides exact JSON payloads for debugging.

<hr>

## 1. ⚠️ Error Types

The API strictly categorizes client and server-side exceptions into four explicit HTTP status codes.

### 1. 404 Not Found

This error occurs when a client attempts to access a non-existent API route or a specific resource that does not exist in the system.

**Example Error Response:**

```json
{
    "success": false,
    "message": "The requested route does not exist.",
    "data": {},
    "meta": {
        "rate_limit": "60 requests per minute.",
        "path": "/sample",
        "help": "Check the API documentation for valid endpoints.",
        "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs"
    },
    "api_version": "1.1.0",
    "timestamp": "2026-06-19T10:44:07.541101+00:00",
    "request_id": "req_09dee9af-de41-4324-a96f-7b31dd9981e1",
    "status_code": 404
}
```

### 2. 405 Method Not Allowed

This error occurs when a client attempts to access a valid API route using an HTTP method that the specific endpoint is not configured to accept.

**Example Error Response:**

```json
{
    "success": false,
    "message": "The HTTP method 'GET' is not allowed for this route.",
    "data": {},
    "meta": {
        "rate_limit": "60 requests per minute.",
        "path": "/v1/language/speech",
        "method": "GET",
        "help": "Ensure you are using the correct HTTP method as defined in the API documentation.",
        "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs/1_introduction.md"
    },
    "api_version": "1.2.0",
    "timestamp": "2026-06-22T06:44:20.088295+00:00",
    "request_id": "req_b3f97617-12a6-47ea-b07a-b0fda3896e63",
    "status_code": 405
}
```

### 3. 422 Unprocessable Entity

Dispatched by the data validation exception handler when an incoming request payload, query string parameters, or headers break Pydantic's structural validation constraints.

**Example Error Response:**

```json
{
    "success": false,
    "message": "The request payload or parameters failed data validation checks.",
    "data": {
        "validation_errors": [
            {
                "location": "query - word",
                "type": "missing",
                "message": "Field required"
            }
        ]
    },
    "meta": {
        "rate_limit": "60 requests per minute.",
        "path": "/v1/language/dictionary",
        "help": "Check the API documentation for valid endpoints and corresponding parameters. If this persists, please open an issue with the request_id.",
        "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs/1_introduction.md",
        "report_issue": "https://github.com/anikethchavare/api.anikethchavare.com/issues"
    },
    "api_version": "1.2.0",
    "timestamp": "2026-06-20T13:07:20.834540+00:00",
    "request_id": "req_b310ab97-1290-4994-ab12-e36a5f014b0f",
    "status_code": 422
}
```

### 4. 429 Too Many Requests

Triggered by the rate limiting middleware when a client exceeds their allocated request quota within a specific window.

**Example Error Response:**

```json
{
    "success": false,
    "message": "Rate limit exceeded. Please try again later.",
    "data": {},
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.0",
    "timestamp": "2026-06-19T10:44:07.541101+00:00",
    "request_id": "req_850f3920-0844-4a07-bfe4-f4401579a2e3",
    "status_code": 429
}
```

### 5. 500 Internal Server Error

Handled entirely by the universal exception handler. This response is dispatched when an unhandled code exception or unexpected runtime failure happens on the backend.

**Example Error Response:**

```json
{
    "success": false,
    "message": "An internal server error occurred. Please try again later.",
    "data": {},
    "meta": {
        "rate_limit": "60 requests per minute.",
        "error_type": "ZeroDivisionError",
        "path": "/sample",
        "report_issue": "https://github.com/anikethchavare/api.anikethchavare.com/issues",
        "help": "If this persists, please open an issue with the request_id."
      
    },
    "api_version": "1.2.0",
    "timestamp": "2026-06-19T10:49:13.933441+00:00",
    "request_id": "req_6d502044-b1f4-4ae6-a1bb-a0da9d281976",
    "status_code": 500
}
```

<hr>

## 2. 🧭 Next Guide

* **[4_request_logging.md](./4_request_logging.md) $\rightarrow$** Learn more about the request and response information that is logged to the PostgreSQL database.