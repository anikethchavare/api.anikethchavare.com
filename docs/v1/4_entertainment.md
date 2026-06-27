# api.anikethchavare.com / docs / v1 / 4_entertainment.md

This document outlines the endpoints available under the `entertainment` utility namespace.

<hr>

## 1. 📡 Endpoints

These endpoints are bound directly to the `app_v1_entertainment` router and operate under the `/entertainment` prefix namespace.

### 1. `/v1/entertainment`
* **Description:** Serves as the introductory entry point to the utility namespace.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * *Returns an empty dictionary `{}` inside the core `data` block.*
* **Query Parameters:** None
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:** None
* **Example Request URL:** `https://api.anikethchavare.com/v1/entertainment`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Welcome to the 'entertainment' utility namespace. Check the documentation for available endpoints.",
    "data": {},
    "meta": {
        "rate_limit": "60 requests per minute.",
        "help": "Check the API v1 documentation (/entertainment) for available endpoints.",
        "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs/v1/4_entertainment.md"
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-25T03:26:07.642544+00:00",
    "request_id": "req_3d236bd6-71d1-4fc8-97fe-4bdeb08ac303",
    "status_code": 200
}
```

### 2. `/v1/entertainment/jokes`
* **Description:** Fetches one or multiple jokes across customizable categories with explicit filtering parameters.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `jokes` *(Array)*: A list containing string payloads for single-line jokes or array tuples containing [setup, delivery] for two-part jokes.
  * `safe` *(Boolean)*: Indicates whether the batch contains content categorized as safe.
* **Query Parameters:**
  * `category` *(StrictStr, Optional)*: A single category or a comma-separated list of target joke sub-pools. Default to `Any`. Allowed entries: `Any`, `Programming`, `Misc`, `Dark`, `Pun`, `Spooky`, `Christmas`.
  * `type` *(Literal, Optional)*: Restricts jokes to a specific formatting structure. Defaults to `null`. Allowed entries: `single`, `twopart`.
  * `blacklist` *(StrictStr, Optional)*: A comma-separated list of sensitive content flags to filter out from the delivery pool. Defaults to `null`. Allowed entries: `nsfw`, `religious`, `political`, `racist`, `sexist`, `explicit`.
  * `amount` *(StrictInt, Optional)*: The total quantity of jokes to serve in a single response array. Must be between `1` and `10`. Defaults to `1`.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:**
  * `422 Unprocessable Entity` (`ValidationError`): Returned when a requested category string or a provided blacklist flag name does not match the strict allowed configuration array lists.
  * `400 Bad Request` (`JokeAPIError`): Dispatched when the upstream engine handles a bad request state or returns an explicit parameter configuration error payload.
  * `502 Bad Gateway` (`UpstreamServiceError`): Dispatched when the external joke provider service (`v2.jokeapi.dev`) is down, unreachable, or returns a non-200 state.
* **Example Request URL:** `https://api.anikethchavare.com/v1/entertainment/jokes?category=Programming&amount=1`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully fetched the jokes.",
    "data": {
        "jokes": [
            [
                "Why is 6 afraid of 7 in hexadecimal Canada?",
                "Because 7 8 9 A"
            ]
        ],
        "safe": true
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-25T03:26:07.642544+00:00",
    "request_id": "req_5608d918-23ba-4c60-a2b7-c5a7b5db7b5b",
    "status_code": 200
}
```

### 3. `/v1/entertainment/fact`
* **Description:** Retrieves generalized trivia statements and random educational knowledge strings from an external facts repository.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `fact` *(String)*: The raw text statement representing the fetched random or contextual fact payload.
* **Query Parameters:**
  * `type` *(Literal, Optional)*: Evaluates whether to extract a completely random historical/scientific fact or pin it explicitly to the daily dataset context. Defaults to `random`. Allowed entries: `random`, `today`.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:**
  * `502 Bad Gateway` (`UpstreamServiceError`): Dispatched when the downstream provider server (`uselessfacts.jsph.pl`) is offline, returns a corrupt payload, or exits with a non-200 HTTP response structure.
* **Example Request URL:** `https://api.anikethchavare.com/v1/entertainment/fact?type=random`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully fetched the fact.",
    "data": {
        "fact": "Leonardo Da Vinci invented the scissors, the helicopter, and many other present day items."
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-25T03:26:07.642544+00:00",
    "request_id": "req_6a4e9646-267e-48c3-ad92-59245d08bb68",
    "status_code": 200
}
```

### 4. `/v1/entertainment/bored`
* **Description:** Fetches an individual randomized activity or a structural array collection of things to do based on category types and participant size.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `activities` *(Array[String])*: A structured list containing the string descriptions of activities matching the queried filters.
* **Query Parameters:**
  * `random` *(StrictBool, Optional)*: Toggles whether to pull a single random activity choice out of the pool or list all configurations. Defaults to `true`.
  * `type` *(Literal, Optional)*: Restricts tasks to a precise behavioral category. Strictly required if `random=false`. Allowed entries: `education`, `recreational`, `social`, `charity`, `cooking`, `relaxation`, `busywork`.
  * `participants` *(Integer, Optional)*: Limits results to tasks built for an explicit count of people. Allowed entries: `1`, `2`, `3`, `4`, `5`, `6`, `8`.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:**
  * `422 Unprocessable Entity` (`ValidationError`): Dispatched if `random` is set to `false` but the mandatory `type` filter parameter is omitted, or if `participants` receives an unallowed integer value.
  * `404 Not Found` (`ActivityNotFound`): Returned when no matching operational choices exist for the combined filter metrics on the server cluster.
  * `502 Bad Gateway` (`UpstreamServiceError`): Dispatched when the underlying microservice proxy connection (`bored-api.appbrewery.com`) is offline, drops frames, or exits with an unhandled state.
* **Example Request URL:** `https://api.anikethchavare.com/v1/entertainment/bored?random=true&type=cooking`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully fetched the activities.",
    "data": {
        "activities": [
            "Prepare homemade pizza from scratch"
        ]
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-25T03:26:07.642544+00:00",
    "request_id": "req_a298be52-4e1a-4d2c-8801-bc8100ff9241",
    "status_code": 200
}
```

### 5. `/v1/entertainment/guess-gender`
* **Description:** Predicts the statistical probability of a gender associated with a given name, with optional demographic localization.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `gender` *(String)*: The predicted gender (`male` or `female`).
  * `probability` *(Float)*: A decimal value between `0.0` and `1.0` indicating the statistical certainty of the prediction.
  * *Note: If the upstream service lacks sufficient data to make a prediction, the `data` block will return an empty dictionary `{}`.*
* **Query Parameters:**
  * `name` *(StrictStr, Required)*: The first or full name to evaluate for gender probability.
  * `country` *(StrictStr, Optional)*: An ISO 3166-1 alpha-2 country code to localize the prediction and improve statistical accuracy.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:**
  * `422 Unprocessable Entity` (`ValidationError`): Dispatched if the `country` parameter is provided but is not exactly 2 characters in length.
  * `502 Bad Gateway` (`UpstreamServiceError`): Dispatched when the underlying microservice proxy connection (`api.genderize.io`) is offline, unreachable, or exits with a non-200 state.
* **Example Request URL:** `https://api.anikethchavare.com/v1/entertainment/guess-gender?name=alex&country=US`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully predicted the gender.",
    "data": {
        "gender": "male",
        "probability": 0.93
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-25T03:26:07.642544+00:00",
    "request_id": "req_b831cd91-5f2b-4d7c-8802-cd8201ff1234",
    "status_code": 200
}
```

### 6. `/v1/entertainment/guess-age`
* **Description:** Predicts the statistical average age associated with a given name, with optional demographic localization.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `age` *(Integer)*: The predicted average age in years.
  * *Note: If the upstream service lacks sufficient data to make a prediction, the `data` block will return an empty dictionary `{}`.*
* **Query Parameters:**
  * `name` *(StrictStr, Required)*: The first or full name to evaluate for age probability.
  * `country` *(StrictStr, Optional)*: An ISO 3166-1 alpha-2 country code to localize the prediction and improve statistical accuracy.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:**
  * `422 Unprocessable Entity` (`ValidationError`): Dispatched if the `country` parameter is provided but is not exactly 2 characters in length.
  * `502 Bad Gateway` (`UpstreamServiceError`): Dispatched when the underlying microservice proxy connection (`api.agify.io`) is offline, unreachable, or exits with a non-200 state.
* **Example Request URL:** `https://api.anikethchavare.com/v1/entertainment/guess-age?name=michael`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully predicted the age.",
    "data": {
        "age": 52
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-25T03:26:07.642544+00:00",
    "request_id": "req_c942de02-6f3c-5e8d-9913-de9312ff5678",
    "status_code": 200
}
```

### 7. `/v1/entertainment/guess-nation`
* **Description:** Predicts a descending list of probable nationalities and their likelihood percentages based on a given name.
* **HTTP Method:** `GET`
* **Response Type & Schema:** `application/json` (JSONResponse)
  * `country` *(Array[Object])*: An array containing prediction objects. Each object contains a `country_id` (String, ISO 3166-1 alpha-2) and a `probability` (Float, 0.0 - 1.0).
  * *Note: If the upstream service lacks sufficient data to make a prediction, the `data` block will return an empty dictionary `{}`.*
* **Query Parameters:**
  * `name` *(StrictStr, Required)*: The first or full name to evaluate for nation probability.
* **Headers Required:** None
* **Request Body Parameters (application/json):** None
* **Custom Rate Limit:** None
* **Possible Local Exceptions:**
  * `502 Bad Gateway` (`UpstreamServiceError`): Dispatched when the underlying microservice proxy connection (`api.nationalize.io`) is offline, unreachable, or exits with a non-200 state.
* **Example Request URL:** `https://api.anikethchavare.com/v1/entertainment/guess-nation?name=michael`
* **Example Request Headers:** None
* **Example Request Body:** None
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully predicted the nation.",
    "data": {
        "country": [
            {
                "country_id": "US",
                "probability": 0.089
            },
            {
                "country_id": "IE",
                "probability": 0.051
            }
        ]
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.2.2",
    "timestamp": "2026-06-25T03:26:07.642544+00:00",
    "request_id": "req_d153ef13-7a4d-6f9e-0024-ef0423aa6789",
    "status_code": 200
}
```

<hr>

## 2. 🧭 Next Guide

Additional feature sets, utility endpoints, and expanded business logic are currently in development and will be documented here as they release.