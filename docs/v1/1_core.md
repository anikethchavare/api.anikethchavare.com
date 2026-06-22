# api.anikethchavare.com / docs / v1 / 1_core.md

This document outlines the core baseline endpoints available under the Version 1 (`/v1`) application router.

**Production Base URL:** `https://api.anikethchavare.com/v1`

<hr>

## 1. 📡 Endpoints

These endpoints are bound directly to the `router_app_v1` router and operate under the `/v1` prefix namespace.

### 1. `/v1`
* **Description:** Serves as the introductory entry point.
* **HTTP Method:** `GET`
* **Response Type:** `application/json` (JSONResponse)
* **Example Request URL:** `https://api.anikethchavare.com/v1`
* **Example Response:**
```json
{
    "success": true,
    "message": "Welcome to Version 1 of the API.",
    "data": {},
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.1",
    "timestamp": "2026-06-19T11:37:05.738455+00:00",
    "request_id": "req_9e7abd1e-548f-4260-a50f-0e3a4e50109e",
    "status_code": 200
}
```

<hr>

## 2. 🧭 Next Guide

* **[2_language.md](./2_language.md) $\rightarrow$** Explore the `language` utility namespace.