# api.anikethchavare.com / docs / 1_introduction.md

Welcome to the documentation of `api.anikethchavare.com`. This is a high-performance, general-purpose public REST API powered by FastAPI and Python.

* **Current Release:** v1.2.1
* **Production Base URL:** `https://api.anikethchavare.com`

<hr>

## 1. 🛡️ Global Security & Network Policy

Every request routed through the API is subject to strict security middleware layers before hitting destination routes:

* **CORS Policy:** Cross-Origin Resource Sharing (CORS) rules are set to allow complete access to the public. This allows any frontend application, mobile app, program, or client script to make requests to the API.
* **Security Headers:** The API automatically injects robust security headers into every single response payload to safeguard transactions.
* **Rate Limiting:** To prevent server degradation and abuse, clients are limited to a strict threshold of **60 requests per minute per IP address**. Exceeding this quota triggers an immediate `429 Too Many Requests` error. Some endpoints might have custom rate limits enforced.

<hr>

## 2. 📡 Endpoints

These base endpoints are attached directly to the underlying application instance within `server.py` and execute independently of any API versioning namespaces.

### 1. `/`
* **Description:** Serves as the introductory entry point.
* **HTTP Method:** `GET`
* **Response Type:** `application/json` (JSONResponse)
* **Example Request URL:** `https://api.anikethchavare.com`
* **Example Response:**
```json
{
    "success": true,
    "message": "A high-performance, general-purpose public REST API powered by FastAPI and Python.",
    "data": {},
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.1",
    "timestamp": "2026-06-19T03:50:27.795509+00:00",
    "request_id": "req_e085e44c-eea3-495c-a9be-bb4e90a6694d",
    "status_code": 200
}
```

### 2. `/favicon.ico`
* **Description:** Retrieves the standard graphic favicon of the API.
* **HTTP Method:** `GET`
* **Response Type:** `image/x-icon` (FileResponse)
* **Example Request URL:** `https://api.anikethchavare.com/favicon.ico`
* **Example Response:** Binary stream of image/x-icon asset.

### 3. `/health`
* **Description:** Performs an operational check to verify the overall health, status, and availability of the API.
* **HTTP Method:** `GET`
* **Response Type:** `application/json` (JSONResponse)
* **Possible Local Exceptions:**
  * `503 Service Unavailable` (`ServiceStatusFailure`): Returned if the application is running but failing its internal service checks.
* **Example Request URL:** `https://api.anikethchavare.com/health`
* **Example Response:**
```json
{
    "success": true,
    "message": "API is healthy and running.",
    "data": {
        "health_checks": {
            "api": "pass",
            "database": "pass"
        }
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.1",
    "timestamp": "2026-06-19T04:01:15.922319+00:00",
    "request_id": "req_742e83f5-044d-4f02-bf52-ecfb2c5e1de9",
    "status_code": 200
}
```

### 4. `/clear-request-logs`
* **Description:** Explicitly clears all transaction history logs from the database. This route is optimized for automated data retention maintenance and is designed to be triggered exclusively by Vercel Cron Jobs.
* **HTTP Method:** `POST`
* **Response Type:** `application/json` (JSONResponse)
* **Headers Required:**
  * `Authorization` *(String, Required)*: A bearer token string formatted as `Bearer <CRON_SECRET>`. This token maps to a private project environment variable to securely isolate administrative functionalities from public clients.
* **Possible Local Exceptions:**
  * `401 Unauthorized`: Returned if the `Authorization` header is entirely missing, improperly formatted, or contains an invalid credential token string.
* **Example Request URL:** `https://api.anikethchavare.com/clear-request-logs`
* **Example Request Headers:**
```http request
Authorization: Bearer secure_cron_secret_token
```
* **Example Response:**
```json
{
    "success": true,
    "message": "Vercel Cron: Request logs successfully deleted.",
    "data": {},
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.1",
    "timestamp": "2026-06-22T06:44:20.088295+00:00",
    "request_id": "req_b3f97617-12a6-47ea-b07a-b0fda3896e63",
    "status_code": 200
}
```

<hr>

## 3. 🧭 Next Guide

* **[2_response_structure.md](./2_response_structure.md) $\rightarrow$** Explore the global response schema and structural JSON examples.