# api.anikethchavare.com / docs / 1_introduction.md

Welcome to the documentation of `api.anikethchavare.com`. This is a high-performance, general-purpose public REST API powered by FastAPI and Python.

* **Current Release:** v1.2.2
* **Production Base URL:** `https://api.anikethchavare.com`

**Documentation Versioning Note:** The code samples, responses, and version references throughout these guides may reflect previous stable releases. For the definitive list of latest additions, patches, and security improvements, please always refer directly to the live **[CHANGELOG.md](../CHANGELOG.md)**.

<hr>

## 1. 🛡️ Global Security & Network Policy

Every request routed  through the API is subject to strict security middleware layers before hitting destination routes:

* **CORS Policy:** Cross-Origin Resource Sharing (CORS) rules are set to allow complete access to the public. This allows any frontend application, mobile app, program, or client script to make requests to the API.
* **Security Headers:** The API automatically injects robust security headers into every single response payload to safeguard transactions.
* **Rate Limiting:** To prevent server degradation and abuse, clients are limited to a strict global threshold of **60 requests per minute per IP address**. Exceeding this quota triggers an immediate `429 Too Many Requests` error. Some endpoints might have custom rate limits enforced.

<hr>

## 2. 📋 Endpoint Documentation Schema

To maintain absolute uniformity across all utility guides, every endpoint blueprint adheres to a predictable sequence. Depending on the route's technical requirements, a combination of the following structural keys is used:

* **`Description`:** A brief summary detailing the purpose and operational behavior of the endpoint.
* **`HTTP Method`:** The required network request verb.
* **`Response Type & Schema`:** The explicit media type header, matching FastAPI response class, and a structured breakdown of the keys returned inside the `data` object payload.
* **`Query Parameters`:** A breakdown of the keys, validation types, and constraints expected in the URL query string.
* **`Headers Required`:** Contextual metadata or security tokens that must be passed inside the network header.
* **`Request Body Parameters (application/json)`:** The strict dictionary payload parameters and constraint rules required for the request body.
* **`Custom Rate Limit`:** A localized threshold that overrides the default global request allowance for specific routes.
* **`Possible Local Exceptions`:** Granular error types or upstream breakdown scenarios unique to the endpoint.
* **`Example Request URL`:** A mock reference illustrating a properly structured destination link.
* **`Example Request Headers`:** A sample key-value preview of an authorized request header block.
* **`Example Request Body`:** A structural JSON snippet illustrating a valid request payload.
* **`Example Response`:** The definitive response returned upon a successful `200 OK` transaction.

<hr>

## 3. 📡 Endpoints

These base endpoints are attached directly to the underlying application instance within `server.py` and execute independently of any API versioning namespaces.

### 1. `/`
* **Description:** Serves as the introductory entry point.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * *Returns an empty dictionary `{}` inside the core `data` block.*
* **Query Parameters:** None
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:** None
* **Example Request URL:** `https://api.anikethchavare.com`
* **Example Request Headers:** None
* **Example Request Body:** None
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

### 2. `/favicon.ico` and `/favicon.png`
* **Description:** Retrieves the standard graphic favicon of the API.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `image/png` (FileResponse)
  * *Returns the raw binary image data of the favicon directly (No structured JSON `data` payload wrapper is used for this file response).*
* **Query Parameters:** None
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:** None
* **Example Request URL:** `https://api.anikethchavare.com/favicon.ico` or `https://api.anikethchavare.com/favicon.png`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:** Binary stream of image/png asset.

### 3. `/health`
* **Description:** Performs an operational check to verify the overall health, status, and availability of the API.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `health_checks` *(Object)*: Nested diagnostics detailing the connectivity health of system backends.
    * `api` *(String)*: Validation status tracking the operational responsiveness of the FastAPI container instance (`pass` or `fail`).
    * `database` *(String)*: Validation status tracking pool connectivity to the persistent relational database layer (`pass` or `fail`).
* **Query Parameters:** None
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:**
  * `503 Service Unavailable` (`ServiceStatusFailure`): Returned if the application is running but failing its internal service checks.
* **Example Request URL:** `https://api.anikethchavare.com/health`
* **Example Request Headers:** None
* **Example Request Body:** None
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
* **Response Type & Schema:** `application/json` (JSONResponse)
  * *Returns an empty dictionary `{}` inside the core `data` block.*
* **Query Parameters:** None
* **Headers Required:**
  * `Authorization` *(String, Required)*: A bearer token string formatted as `Bearer <CRON_SECRET>`. This token maps to a private project environment variable to securely isolate administrative functionalities from public clients.
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:**
  * `401 Unauthorized`: Returned if the `Authorization` header is entirely missing, improperly formatted, or contains an invalid credential token string.
* **Example Request URL:** `https://api.anikethchavare.com/clear-request-logs`
* **Example Request Headers:**
```http request
Authorization: Bearer secure_cron_secret_token
```
* **Example Request Body:** None
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

## 4. 🕦 Automated Maintenance

The API features built-in self-cleaning pipelines managed via Vercel Cron jobs.

### Request Log Cleanup
* **Endpoint:** `/clear-request-logs`
* **Execution Interval:** Managed via `vercel.json` configurations.
* **Security:** This endpoint strictly requires a `CRON_SECRET` sent via authorization headers matching the infrastructure environment variables. Unauthorized or manual requests without the correct signing key will return a `401 Unauthorized` response.

<hr>

## 5. 🧭 Next Guide

* **[2_response_structure.md](./2_response_structure.md) $\rightarrow$** Explore the global response schema and structural JSON examples.