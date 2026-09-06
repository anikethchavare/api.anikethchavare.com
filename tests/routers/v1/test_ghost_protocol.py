# api.anikethchavare.com - tests/routers/v1/test_ghost_protocol.py

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
from server import app

from types import SimpleNamespace
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, MagicMock, patch

# Initializing the TestClient
client = TestClient(app)

# Test Route 1: Main (app_v1_ghost_protocol)
def test_app_v1_ghost_protocol_main():
    """ Tests the ghost-protocol utility namespace root entry point (GET /v1/ghost-protocol/). """

    response = client.get("/v1/ghost-protocol/")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "Welcome to the 'ghost-protocol' utility namespace" in response.json()["message"]
    assert response.json()["meta"]["docs"] == "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs/v1/5_ghost_protocol.md"

# Test Route 2: Generate Token (app_v1_ghost_protocol)
def test_app_v1_ghost_protocol_generate_token_missing_fields():
    """ Tests validation failure when required request body fields are missing. """

    payload = {
        "client_id": "client-123",
        "room_id": "room-abc"
        # missing 'username' and 'action'
    }

    response = client.request("GET", "/v1/ghost-protocol/generate-token", json=payload)
    assert response.status_code == 422
    assert response.json()["success"] is False

@patch("routers.v1.ghost_protocol.ably_client")
def test_app_v1_ghost_protocol_generate_token_presence_failure(mock_ably):
    """ Tests internal server error handling when presence retrieval fails (500 Handling). """

    mock_channel = MagicMock()
    mock_channel.presence.get = AsyncMock(side_effect=Exception("Ably connection error"))
    mock_ably.channels.get.return_value = mock_channel

    payload = {
        "client_id": "client-123",
        "room_id": "room-abc",
        "username": "agent-47",
        "action": "create"
    }

    response = client.request("GET", "/v1/ghost-protocol/generate-token", json=payload)
    assert response.status_code == 500
    assert response.json()["success"] is False
    assert "Failed to validate room metadata status." in response.json()["message"]

@patch("routers.v1.ghost_protocol.ably_client")
def test_app_v1_ghost_protocol_generate_token_join_room_not_found(mock_ably):
    """ Tests validation error when attempting to join a non-existent or empty room (404 Handling). """

    mock_channel = MagicMock()
    mock_channel.presence.get = AsyncMock(return_value=SimpleNamespace(items=[]))
    mock_ably.channels.get.return_value = mock_channel

    payload = {
        "client_id": "client-123",
        "room_id": "nonexistent-room",
        "username": "agent-47",
        "action": "join"
    }

    response = client.request("GET", "/v1/ghost-protocol/generate-token", json=payload)
    assert response.status_code == 404
    assert response.json()["success"] is False
    assert "The room ID does not exist or is inactive." in response.json()["message"]

@patch("routers.v1.ghost_protocol.ably_client")
def test_app_v1_ghost_protocol_generate_token_username_conflict(mock_ably):
    """ Tests rejection when a username is already active in the room (409 Handling). """

    mock_ably.channels.get.return_value.presence.get = AsyncMock(return_value=SimpleNamespace(items=[SimpleNamespace(data="Ghost-Rider")]))

    payload = {
        "client_id": "client-123",
        "room_id": "active-room",
        "username": "Ghost Rider ",
        "action": "create"
    }

    response = client.request("GET", "/v1/ghost-protocol/generate-token", json=payload)
    assert response.status_code == 409
    assert response.json()["success"] is False
    assert "The username is already taken by another active member." in response.json()["message"]

@patch("routers.v1.ghost_protocol.ably_client")
def test_app_v1_ghost_protocol_generate_token_success_create(mock_ably):
    """ Tests successful token generation when creating a new room (action: create). """

    mock_channel = MagicMock()
    mock_channel.presence.get = AsyncMock(return_value=SimpleNamespace(items=[]))
    mock_ably.channels.get.return_value = mock_channel

    mock_token_request = MagicMock()
    mock_token_request.to_dict.return_value = {
        "keyName": "key-id",
        "token": "tok-create-123"
    }
    mock_ably.auth.create_token_request = AsyncMock(return_value=mock_token_request)

    payload = {
        "client_id": "client-101",
        "room_id": "room-new",
        "username": "agent-ethan",
        "action": "create"
    }

    response = client.request("GET", "/v1/ghost-protocol/generate-token", json=payload)
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "Successfully generated the Ably token." in response.json()["message"]
    assert response.json()["data"]["token"] == "tok-create-123"

    mock_ably.auth.create_token_request.assert_awaited_once_with({
        "client_id": "client-101",
        "capability": {
            "room:room-new": ["publish", "subscribe", "presence", "channel-metadata"]
        }
    })

@patch("routers.v1.ghost_protocol.ably_client")
def test_app_v1_ghost_protocol_generate_token_success_join(mock_ably):
    """ Tests successful token generation when joining an active room (action: join). """

    mock_channel = MagicMock()
    mock_channel.presence.get = AsyncMock(return_value=SimpleNamespace(items=[SimpleNamespace(data="agent-ethan")]))
    mock_ably.channels.get.return_value = mock_channel

    mock_token_request = MagicMock()
    mock_token_request.to_dict.return_value = {
        "keyName": "key-id",
        "token": "tok-join-456"
    }
    mock_ably.auth.create_token_request = AsyncMock(return_value=mock_token_request)

    payload = {
        "client_id": "client-202",
        "room_id": "room-active",
        "username": "agent-luther",
        "action": "join"
    }

    response = client.request("GET", "/v1/ghost-protocol/generate-token", json=payload)
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "Successfully generated the Ably token." in response.json()["message"]
    assert response.json()["data"]["token"] == "tok-join-456"

    mock_ably.auth.create_token_request.assert_awaited_once_with({
        "client_id": "client-202",
        "capability": {
            "room:room-active": ["publish", "subscribe", "presence", "channel-metadata"]
        }
    })