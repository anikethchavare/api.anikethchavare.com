# api.anikethchavare.com - tests/routers/v1/test_entertainment.py

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

# Test Route 1: Main (app_v1_entertainment)
def test_app_v1_entertainment_main():
    """ Tests the entertainment utility namespace root entry point (GET /v1/entertainment/). """

    response = client.get("/v1/entertainment/")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "Welcome to the 'entertainment' utility namespace" in response.json()["message"]

# Test Routes 2: Jokes (app_v1_entertainment)
@respx.mock
def test_app_v1_entertainment_jokes_success_single():
    """ Tests a successful fetch of a single-type joke. """

    mock_response = {
        "error": False,
        "amount": 1,
        "jokes": [
            {
                "category": "Programming",
                "type": "single",
                "joke": "Variables de-allocated, memory freed. Rest in peace.",
                "safe": True,
                "id": 1
            }
        ]
    }

    respx.get("https://v2.jokeapi.dev/joke/Any").mock(
        return_value=httpx.Response(200, json=mock_response)
    )

    response = client.get("/v1/entertainment/jokes")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["data"]["jokes"][0] == "Variables de-allocated, memory freed. Rest in peace."
    assert response.json()["data"]["safe"] is True

@respx.mock
def test_app_v1_entertainment_jokes_success_twopart():
    """ Tests a successful fetch of a two-part joke structure. """

    mock_response = {
        "error": False,
        "amount": 1,
        "jokes": [
            {
                "category": "Pun",
                "type": "twopart",
                "setup": "Why do we tell actors to 'break a leg'?",
                "delivery": "Because every play has a cast.",
                "safe": True,
                "id": 2
            }
        ]
    }

    respx.get("https://v2.jokeapi.dev/joke/Pun").mock(
        return_value=httpx.Response(200, json=mock_response)
    )

    response = client.get("/v1/entertainment/jokes?category=Pun&type=twopart")
    assert response.status_code == 200
    assert response.json()["data"]["jokes"][0] == ["Why do we tell actors to 'break a leg'?", "Because every play has a cast."]

def test_app_v1_entertainment_jokes_invalid_category():
    """ Tests the internal validation guard when an invalid joke category is provided. """

    response = client.get("/v1/entertainment/jokes?category=InvalidCategory")
    assert response.status_code == 422
    assert response.json()["success"] is False
    assert "Validation Error" in response.json()["message"]

def test_app_v1_entertainment_jokes_invalid_blacklist():
    """ Tests the internal validation guard when an invalid blacklist flag is provided. """

    response = client.get("/v1/entertainment/jokes?blacklist=clean")
    assert response.status_code == 422
    assert response.json()["success"] is False
    assert "Validation Error" in response.json()["message"]

@respx.mock
def test_app_v1_entertainment_jokes_upstream_failure():
    """ Tests error mapping rules when JokeAPI experiences upstream errors (502 Handling). """

    respx.get("https://v2.jokeapi.dev/joke/Any").mock(
        return_value=httpx.Response(500)
    )

    response = client.get("/v1/entertainment/jokes")
    assert response.status_code == 502
    assert response.json()["success"] is False
    assert "unexpected error occurred while fetching the jokes" in response.json()["message"]

@respx.mock
def test_app_v1_entertainment_jokes_api_level_error():
    """ Tests handling when JokeAPI responds 200 OK but includes an error payload (400 Handling). """

    mock_error_payload = {
        "error": True,
        "additionalInfo": "Query parameter 'amount' must be an integer between 1 and 10."
    }

    respx.get("https://v2.jokeapi.dev/joke/Any").mock(
        return_value=httpx.Response(200, json=mock_error_payload)
    )

    response = client.get("/v1/entertainment/jokes?amount=10")
    assert response.status_code == 400
    assert response.json()["success"] is False
    assert "JokeAPI Error" in response.json()["message"]

# Test Routes 3: Fact (app_v1_entertainment)
@respx.mock
def test_app_v1_entertainment_fact_random_success():
    """ Tests successfully retrieving a random useless fact. """

    mock_fact_payload = {
        "id": "abc-123",
        "text": "The total volume of water in the oceans is about 1.3 billion cubic kilometers.",
        "source": "djtech.net",
        "source_url": "https://example.com",
        "language": "en",
        "permalink": "https://example.com"
    }

    respx.get("https://uselessfacts.jsph.pl/api/v2/facts/random").mock(
        return_value=httpx.Response(200, json=mock_fact_payload)
    )

    response = client.get("/v1/entertainment/fact?type=random")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "text" not in response.json()["data"]
    assert response.json()["data"]["fact"] == "The total volume of water in the oceans is about 1.3 billion cubic kilometers."

@respx.mock
def test_app_v1_entertainment_fact_upstream_failure():
    """ Tests safety wrappers when the facts engine suffers internal breakdowns (502 Handling). """

    respx.get("https://uselessfacts.jsph.pl/api/v2/facts/today").mock(
        return_value=httpx.Response(504)
    )

    response = client.get("/v1/entertainment/fact?type=today")
    assert response.status_code == 502
    assert response.json()["success"] is False
    assert "unexpected error occurred while fetching the fact" in response.json()["message"]

# Test Routes 4: Bored (app_v1_entertainment)
@respx.mock
def test_app_v1_entertainment_bored_random_success():
    """ Tests a successful fetch of a completely random activity. """

    mock_response = {
        "activity": "Learn a new magic trick",
        "type": "recreational",
        "participants": 1,
        "price": 0,
        "link": "",
        "key": "8130283",
        "accessibility": 0
    }

    respx.get("https://bored-api.appbrewery.com/random").mock(
        return_value=httpx.Response(200, json=mock_response)
    )

    response = client.get("/v1/entertainment/bored?random=true")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["data"]["activities"] == ["Learn a new magic trick"]

@respx.mock
def test_app_v1_entertainment_bored_filter_success():
    """ Tests a successful fetch of filtered activities when random is false. """

    mock_response = [
        {
            "activity": "Bake a chocolate soufflé",
            "type": "cooking",
            "participants": 2
        },
        {
            "activity": "Prepare homemade pizza from scratch",
            "type": "cooking",
            "participants": 2
        }
    ]

    respx.get("https://bored-api.appbrewery.com/filter?type=cooking&participants=2").mock(
        return_value=httpx.Response(200, json=mock_response)
    )

    response = client.get("/v1/entertainment/bored?random=false&type=cooking&participants=2")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert isinstance(response.json()["data"]["activities"], list)
    assert "Bake a chocolate soufflé" in response.json()["data"]["activities"]
    assert len(response.json()["data"]["activities"]) == 2

def test_app_v1_entertainment_bored_missing_type_validation():
    """ Tests the internal guardrail rejecting non-random requests lacking a type parameter. """

    response = client.get("/v1/entertainment/bored?random=false")
    assert response.status_code == 422
    assert response.json()["success"] is False
    assert "Validation Error" in response.json()["message"]

@respx.mock
def test_app_v1_entertainment_bored_not_found():
    """ Tests error mapping rules when the filters yield no matches (404 Handling). """

    respx.get("https://bored-api.appbrewery.com/filter?type=charity&participants=8").mock(
        return_value=httpx.Response(404)
    )

    response = client.get("/v1/entertainment/bored?random=false&type=charity&participants=8")
    assert response.status_code == 404
    assert response.json()["success"] is False
    assert "No activities found matching the specified parameters" in response.json()["message"]

@respx.mock
def test_app_v1_entertainment_bored_upstream_failure():
    """ Tests safety wrappers when the downstream mirror suffers connection faults (502 Handling). """

    respx.get("https://bored-api.appbrewery.com/random").mock(
        return_value=httpx.Response(503)
    )

    response = client.get("/v1/entertainment/bored?random=true")
    assert response.status_code == 502
    assert response.json()["success"] is False
    assert "unexpected error occurred while fetching the activity" in response.json()["message"]