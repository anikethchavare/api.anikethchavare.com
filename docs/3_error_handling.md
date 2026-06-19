# api.anikethchavare.com / docs / 3_error_handling.md

This document serves as a comprehensive reference for the various error types and HTTP exception states a client might encounter while interacting with the API. It details the structural format of failure responses and provides exact JSON payloads for debugging.

<hr>

## 1. ⚠️ Error Types

The API strictly categorizes client and server-side exceptions into four explicit HTTP status codes.

### 1. 404 Not Found

This error occurs when a client attempts to access a non-existent API route or a specific resource that does not exist in the system.

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
    "api_version": "1.0.0",
    "timestamp": "2026-06-19T10:44:07.541101+00:00",
    "request_id": "req_09dee9af-de41-4324-a96f-7b31dd9981e1",
    "status_code": 404
}
```

### 2. 429 Too Many Requests

Triggered by the rate limiting middleware when a client exceeds their allocated request quota within a specific window.

```json
{
    "success": false,
    "message": "Rate limit exceeded. Please try again later.",
    "data": {},
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.0.0",
    "timestamp": "2026-06-19T10:44:07.541101+00:00",
    "request_id": "req_850f3920-0844-4a07-bfe4-f4401579a2e3",
    "status_code": 429
}
```

### 3. 500 Internal Server Error

Handled entirely by the universal exception handler. This response is dispatched when an unhandled code exception or unexpected runtime failure happens on the backend.

```json
{
    "success": false,
    "message": "An internal server error occurred. Please try again later.",
    "data": {},
    "meta": {
        "rate_limit": "60 requests per minute.",
        "error_type": "ZeroDivisionError: Cannot divide by zero.",
        "path": "/sample",
        "report_issue": "https://github.com/anikethchavare/api.anikethchavare.com/issues",
        "help": "If this persists, please open an issue with the request_id."
      
    },
    "api_version": "1.0.0",
    "timestamp": "2026-06-19T10:49:13.933441+00:00",
    "request_id": "req_6d502044-b1f4-4ae6-a1bb-a0da9d281976",
    "status_code": 500
}
```

### 4. 503 Service Unavailable

Sent when the API is running but unable to fulfill requests due to temporary downstream factors, such as database connection dropouts, high server capacity overload, or scheduled maintenance windows.

```json
{
    "success": false,
    "message": "API is unhealthy and non-responsive. One or more internal services are currently unavailable.",
    "data": {
        "health_checks": {
            "api": "fail",
            "database": "fail"
        }
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.0.0",
    "timestamp": "2026-06-19T10:53:52.972973+00:00",
    "request_id": "req_bb526ca8-feac-495b-a8f1-e3fb98be1f4e",
    "status_code": 503
}
```

<hr>

## 2. 🧭 Next Guide

* **[4_request_logging.md](./4_request_logging.md) $\rightarrow$** Learn more about the request and response information that is logged to the PostgreSQL database.