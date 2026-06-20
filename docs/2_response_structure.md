# api.anikethchavare.com / docs / 2_response_structure.md

This document defines the global JSON response structure utilized by the API. Every response adheres to this consistent contract to ensure seamless client-side parsing.

<hr>

## 1. 📋 Response Schema

| Field | Type | Description                                                                                                     |
| :--- | :--- |:----------------------------------------------------------------------------------------------------------------|
| **`success`** | `Boolean` | Indicates whether the request succeeded (`true`) or failed (`false`).                                           |
| **`message`** | `String` / `Object` | A human-readable message for successful requests, or a structured error object for failures.                    |
| **`data`** | `Object` / `Array` | The primary payload of the response (can be empty if no payload is returned).                                   |
| **`meta`** | `Object` / `Array` | Contextual metadata including rate limit thresholds and other information. |
| **`api_version`** | `String` | The current API version string (e.g., `1.0.0`).                                                                 |
| **`timestamp`** | `String` | The UTC timestamp of the response execution in ISO 8601 format.                                                 |
| **`request_id`** | `String` | A unique identifier prefixed with `req_` used for trace logging and server-side debugging.                      |
| **`status_code`** | `Integer` | The explicit HTTP status code matching the response header.                                                     |

<hr>

## 2. 🧭 Next Guide

* **[3_global_error_handling.md](./3_global_error_handling.md) $\rightarrow$** Explore the API error codes, the universal exception handler, and layouts for 404 and rate limiting errors.