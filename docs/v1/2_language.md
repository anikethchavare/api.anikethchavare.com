# api.anikethchavare.com / docs / v1 / 2_language.md

This document outlines the endpoints available under the `language` utility namespace.

<hr>

## 1. 📡 Endpoints

These endpoints are bound directly to the `app_v1_language` router and operate under the `/language` prefix namespace.

### 1. `/`
* **Description:** Serves as the introductory entry point to the namespace.
* **HTTP Method:** `GET`
* **Response Type:** `application/json` (JSONResponse)
* **Example Request URL:** `https://api.anikethchavare.com/v1/language`
* **Example Response:**
```json
{
    "success": true,
    "message": "Welcome to the 'language' utility namespace. Check the documentation for available endpoints.",
    "data": {},
    "meta": {
        "rate_limit": "60 requests per minute.",
        "help": "Check the API v1 documentation (/language) for available endpoints.",
        "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs/v1/2_language.md"
    },
    "api_version": "1.1.0",
    "timestamp": "2026-06-20T13:13:15.403122+00:00",
    "request_id": "req_663a8a12-ea1e-46c0-a4e1-ac0b85cdd601",
    "status_code": 200
}
```

### 2. `/dictionary?word=<word>&phonetics=<boolean>&definitions=<boolean>&strict=<boolean>`
* **Description:** Queries detailed linguistic data for a given English word, including phonetics, parts of speech, and definitions from an external dictionary provider.
* **HTTP Method:** `GET`
* **Response Type:** `application/json` (JSONResponse)
* **Query Parameters:**
  * `word` *(StrictStr, Required)*: The target English word to look up in the dictionary. Must be at least 1 character long.
  * `phonetics` *(StrictBool, Optional)*: Toggles whether the phonetic transcriptions and audio URLs are returned. Defaults to `true`.
  * `definitions` *(StrictBool, Optional)*: Toggles whether the dictionary definitions section is included. Defaults to `true`.
  * `strict` *(StrictBool, Optional)*: Modifies the `definitions` payload to output a flat list of string definitions rather than a structured object grouped by parts of speech. Only applies if `definitions=true`. Defaults to `false`.
* **Possible Local Exceptions:**
  * `404 Not Found` (`WordNotFound`): Returned when the target word is spelled incorrectly or does not exist within the external dictionary database.
  * `502 Bad Gateway` (`UpstreamServiceError`): Dispatched when the external dictionary provider API (`api.dictionaryapi.dev`) is down, unreachable, or returns an unexpected server error.
* **Example Request URL:** `https://api.anikethchavare.com/v1/language/dictionary?word=hello&phonetics=false&strict=true`
* **Example Response:**
```json
{
    "success": true,
    "message": "Successfully queried the dictionary for the word.",
    "data": {
        "word": "hello",
        "phonetics": null,
        "definitions": [
            "\"Hello!\" or an equivalent greeting.",
            "To greet with \"hello\".",
            "A greeting (salutation) said when meeting someone or acknowledging someone’s arrival or presence.",
            "A greeting used when answering the telephone.",
            "A call for response if it is not clear if anyone is present or listening, or if a telephone conversation may have been disconnected.",
            "Used sarcastically to imply that the person addressed or referred to has done something the speaker or writer considers to be foolish.",
            "An expression of puzzlement or discovery."
        ],
        "license": {
            "name": "CC BY-SA 3.0",
            "url": "https://creativecommons.org/licenses/by-sa/3.0"
        },
        "source_urls": [
            "https://en.wiktionary.org/wiki/hello"
        ]
    },
    "meta": {
        "rate_limit": "60 requests per minute."
    },
    "api_version": "1.0.0",
    "timestamp": "2026-06-20T13:19:18.008099+00:00",
    "request_id": "req_eb41dfeb-1762-4b0e-8ede-3005e24a98ba",
    "status_code": 200
}
```

### 3. `/speech`
* **Description:** Converts custom English text content into a high-quality, synthesized spoken audio file stream using premium Microsoft neural AI voice models.
* **HTTP Method:** `POST`
* **Response Type:** `audio/mpeg` (StreamingResponse)
* **Request Body Parameters (`application/json`):**
  * `text` *(String, Required)*: The primary English text payload to be converted into speech. Minimum length of 1 character, maximum length of 500 characters.
  * `voice` *(String, Optional)*: The short-name identifier of the target neural voice model. Defaults to `en-US-ChristopherNeural`.
  * `rate` *(String, Optional)*: The relative speaking tempo/speed modification percentage string. Defaults to `+0%`.
  * `pitch` *(String, Optional)*: The relative structural vocal frequency pitch adjustment string. Defaults to `+0Hz`.
* **Possible Local Exceptions:**
  * `502 Bad Gateway` (`UpstreamServiceError`): Dispatched when the underlying Microsoft Edge TTS communication loop fails, drops, or encounters an upstream connection exception.
* **Example Request URL:** `https://api.anikethchavare.com/v1/language/speech`
* **Example Request Body:**
```json
{
    "text": "Hello, welcome to the language namespace utility.",
    "voice": "en-US-AnaNeural",
    "rate": "+10%",
    "pitch": "-5Hz"
}
```
* **Example Response:** Binary data stream of the generated `audio/mpeg` asset (MP3 file).

<hr>

## 2. 🧭 Next Guide

Additional feature sets, utility endpoints, and expanded business logic are currently in development and will be documented here as they release.