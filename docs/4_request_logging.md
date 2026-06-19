# api.anikethchavare.com / docs / 4_request_logging.md

This document defines the telemetry pipeline and PostgreSQL schema used to log API transactions. It's used for historical auditing and performance tracking.

<hr>

## 1. 📊 Logging Schema

The table below defines the exact data points extracted from the network lifecycle and saved into the PostgreSQL logging table.

| Column Name | Data Type                  | Source | Description |
| :--- |:---------------------------| :--- | :--- |
| `request_id` | `TEXT`                     | Middleware | The unique identifier tracking the lifecycle of the transaction. |
| `success` | `BOOLEAN`                  | HTTP Response | Indicates whether the API request was completed successfully. |
| `message` | `TEXT`                     | HTTP Response | The human-readable string message explaining the outcome of the transaction. |
| `data` | `JSONB`                    | HTTP Response | The internal payload object containing the core response data. |
| `meta` | `JSONB`                    | HTTP Response | Contextual metadata object containing extra fields (e.g., rate limits, errors). |
| `api_version` | `TEXT`                     | Application | The semantic version of the running API instance. |
| `timestamp` | `TIMESTAMP WITH TIME ZONE` | Middleware | The exact date and time the transaction was processed (UTC). |
| `status_code` | `INTEGER`                  | HTTP Response | The final HTTP status code returned to the client (e.g., `200`, `404`, `500`). |
| `ip_address` | `TEXT`                     | HTTP Header | The IP address of the client making the request (supports IPv4 and IPv6). |
| `user_agent` | `TEXT`                     | HTTP Header | The client application or browser details initiating the network request. |
| `origin` | `TEXT`                     | HTTP Header | The domain or scheme where the request originated from (CORS indicator). |
| `path` | `TEXT`                     | HTTP Request | The absolute path endpoint targeted by the client (e.g., `/v1/sample`). |
| `vercel_execution_id` | `TEXT`                     | Environment | The specific internal function execution ID assigned by the Vercel serverless platform. |
| `http_version` | `TEXT`                     | HTTP Request | The HTTP protocol version used for the connection (e.g., `1.1`, `2`). |

<hr>

## 2. 🧭 Next Guide

* **[5_setup.md](./5_setup.md) $\rightarrow$** Proceed to the setup guide to learn how to clone, configure, and deploy the complete API application locally.