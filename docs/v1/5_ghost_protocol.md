# api.anikethchavare.com / docs / v1 / 5_ghost_protocol.md

This document outlines the endpoints available under the `ghost-protocol` utility namespace.

<hr>

## 1. 📡 Endpoints

These endpoints are bound directly to the `app_v1_ghost_protocol` router and operate under the `/ghost-protocol` prefix namespace.

### 1. `/v1/ghost-protocol`
* **Description:** Serves as the introductory entry point to the utility namespace.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * *Returns an empty dictionary `{}` inside the core `data` block.*
* **Query Parameters:** None
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:** None
* **Example Request URL:** `https://api.anikethchavare.com/v1/ghost-protocol`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Welcome to the 'ghost-protocol' utility namespace. Check the documentation for available endpoints.",
    "data": {},
    "meta": {
        "rate_limit": "60 requests per minute.",
        "help": "Check the API v1 documentation (/ghost-protocol) for available endpoints.",
        "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs/v1/5_ghost_protocol.md"
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-25T03:26:07.642544+00:00",
    "request_id": "req_8e4a5d12-9c3f-421b-87ae-123456abcdef",
    "status_code": 200
}
```

### 2. `/v1/ghost-protocol/generate-token`
* **Description:** Generates an Ably authentication token request with room-scoped capabilities after validating room existence and username availability.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `keyName` *(String)*: The public key identifier component of the Ably API key.
  * `clientId` *(String)*: The explicit client identifier bound to the session.
  * `ttl` *(Integer, Optional)*: Time-to-live parameter for the requested token in milliseconds.
  * `nonce` *(String)*: A unique, unquoted cryptographic random string used to prevent replay attacks.
  * `capability` *(String)*: Stringified JSON dictionary defining permitted operations (`publish`, `subscribe`, `presence`, `channel-metadata`) scoped to `room:{room_id}`.
  * `timestamp` *(Integer)*: Epoch timestamp when the token request was issued.
  * `mac` *(String)*: Message Authentication Code signature confirming token authenticity.
* **Query Parameters:** None
* **Headers Required:** None
* **Request Body Parameters (application/json):**
  * `client_id` *(StrictStr, Required)*: The unique identifier representing the connecting client instance.
  * `room_id` *(StrictStr, Required)*: The target room identifier namespace to bind presence and access tokens to.
  * `username` *(StrictStr, Required)*: The member's designated handle. Whitespace will be normalized into hyphens during presence collision evaluation.
  * `action` *(StrictStr, Required)*: The room connection mode. Must be either `create` or `join`.
* **Custom Rate Limit:** None
* **Possible Local Exceptions:**
  * `404 Not Found`: Dispatched when `action` is set to `join` but the target channel room has no active presence members or does not exist.
  * `409 Conflict`: Dispatched when the requested `username` matches an active presence member already in the room.
  * `422 Unprocessable Entity` (`ValidationError`): Dispatched when any required payload body key is missing or is assigned an invalid data type.
  * `500 Internal Server Error`: Dispatched when the upstream Ably transport interface encounters a connectivity failure or throws an unhandled error while inspecting channel presence.
* **Example Request URL:** `https://api.anikethchavare.com/v1/ghost-protocol/generate-token`
* **Example Request Headers:** None
* **Example Request Body:**
```json
{
    "client_id": "client_c049b13c-74ae",
    "room_id": "alpha-protocol-402",
    "username": "Ethan-Hunt",
    "action": "create"
}
```
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully generated the Ably token.",
    "data": {
        "keyName": "ABLY_KEY_ID",
        "clientId": "client_c049b13c-74ae",
        "ttl": null,
        "nonce": "n0nc3_r4nd0m_str1ng_98234",
        "capability": "{\"room:alpha-protocol-402\":[\"publish\",\"subscribe\",\"presence\",\"channel-metadata\"]}",
        "timestamp": 1788676329072,
        "mac": "Ww0Z3Kj5T+x3kL28B99JklL0z/jKL9=="
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-25T03:26:07.642544+00:00",
    "request_id": "req_f4a13e28-1b9a-4d76-b605-728bceba9102",
    "status_code": 200
}
```

<hr>

## 2. 🧭 Next Guide

Additional feature sets, utility endpoints, and expanded business logic are currently in development and will be documented here as they release.