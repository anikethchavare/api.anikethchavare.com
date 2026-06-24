# api.anikethchavare.com - tests/routers/v1/test_language.py

"""
Copyright 2026 Aniketh Chavare (anikethchavare@zohomail.in)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# Imports
import respx
import httpx
from server import app
from fastapi.testclient import TestClient

# Initializing the TestClient
client = TestClient(app)

# Test Route 1: Main (app_v1_language)
def test_app_v1_language_main():
    """ Tests the language utility namespace root entry point (GET /v1/language/). """

    response = client.get("/v1/language/")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "Welcome to the 'language' utility namespace" in response.json()["message"]

# Test Routes 2: Dictionary (app_v1_language)
@respx.mock
def test_app_v1_language_dictionary_success():
    """ Tests a successful dictionary lookup using a mocked external API response. """

    mock_response_payload = [{
        "word": "test",
        "phonetics": [{"text": "/test/", "audio": ""}],
        "meanings": [{
            "partOfSpeech": "noun",
            "definitions": [{"definition": "A procedure intended to establish the quality."}]
        }],
        "license": {"name": "CC BY-SA 3.0", "url": "https://example.com"},
        "sourceUrls": ["https://example.com"]
    }]

    respx.get("https://api.dictionaryapi.dev/api/v2/entries/en/test").mock(
        return_value=httpx.Response(200, json=mock_response_payload)
    )

    response = client.get("/v1/language/dictionary?word=test")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["data"]["word"] == "test"
    assert isinstance(response.json()["data"]["definitions"], list)

@respx.mock
def test_app_v1_language_dictionary_strict_mode():
    """ Tests the dictionary lookup under 'strict=True' to ensure definitions are flat strings. """

    mock_response_payload = [{
        "word": "test",
        "phonetics": [],
        "meanings": [{
            "partOfSpeech": "noun",
            "definitions": [{"definition": "A standalone procedure description."}]
        }]
    }]

    respx.get("https://api.dictionaryapi.dev/api/v2/entries/en/test").mock(
        return_value=httpx.Response(200, json=mock_response_payload)
    )

    response = client.get("/v1/language/dictionary?word=test&strict=true")
    assert response.status_code == 200
    assert response.json()["data"]["definitions"][0] == "A standalone procedure description."

@respx.mock
def test_app_v1_language_dictionary_not_found():
    """ Tests error mapping rules when a target word does not exist (404 Handling). """

    respx.get(
        "https://api.dictionaryapi.dev/api/v2/entries/en/unknownword").mock(
        return_value=httpx.Response(404)
    )

    response = client.get("/v1/language/dictionary?word=unknownword")
    assert response.status_code == 404
    assert response.json()["success"] is False
    assert "No data was found for the word" in response.json()["message"]

@respx.mock
def test_app_v1_language_dictionary_upstream_failure():
    """ Tests error safety wrappers when the dictionary API suffers internal breakdowns (502 Handling). """

    respx.get("https://api.dictionaryapi.dev/api/v2/entries/en/test").mock(
        return_value=httpx.Response(500)
    )

    response = client.get("/v1/language/dictionary?word=test")
    assert response.status_code == 502
    assert response.json()["success"] is False
    assert "unexpected error occurred while querying the dictionary" in response.json()["message"]

# Test Routes 3: Speech (app_v1_language)
def test_app_v1_language_speech_success():
    """ Tests successful binary voice generation synthesis text piping (POST /v1/language/speech). """

    payload = {
        "text": "Hello world",
        "voice": "en-US-ChristopherNeural",
        "rate": "+0%",
        "pitch": "+0Hz"
    }

    response = client.post("/v1/language/speech", json=payload)
    assert response.status_code == 200
    assert response.headers["content-type"] == "audio/mpeg"

def test_app_v1_language_speech_validation_failure():
    """ Tests safety triggers when input payload string rules are violated (422 Handling). """

    payload = {
        "text": ""
    }

    response = client.post("/v1/language/speech", json=payload)
    assert response.status_code == 422
    assert response.json()["success"] is False