# api.anikethchavare.com - tests/test_server.py

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
from app.config import settings
from fastapi.testclient import TestClient

# Initializing the TestClient
client = TestClient(app)

# Test Route 1: Main (app)
def test_app_main():
    """ Tests the public root entry point (GET /). """

    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "REST API powered by FastAPI and Python" in response.json()["message"]

# Test Route 2: favicon.ico (app)
def test_app_favicon():
    """ Tests graphic favicon retrieval (GET /favicon.ico). """

    response = client.get("/favicon.ico")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"

# Test Route 3: Health (app)
def test_app_health():
    """ Tests operational diagnostics check (GET /health). """

    response = client.get("/health")
    assert response.status_code in [200, 503]
    assert "health_checks" in response.json()["data"]

# Test Routes 4: Clear Request Logs (app)
def test_app_clear_request_logs_unauthorized():
    """ Tests log deletion without valid token signature (POST /clear-request-logs). """

    response = client.post("/clear-request-logs", headers={"Authorization": "Bearer invalid_secret"})
    assert response.status_code == 401
    assert response.json()["success"] is False

def test_app_clear_request_logs_authorized(monkeypatch):
    """ Tests log deletion with valid token signature using mock settings (POST /clear-request-logs). """

    test_secret = "test_cron_secret_key"
    monkeypatch.setattr(settings, "cron_secret", test_secret)

    response = client.post("/clear-request-logs", headers={"Authorization": f"Bearer {test_secret}"})
    assert response.status_code == 200
    assert response.json()["success"] is True

# Test Exception Handler 1: 429 (app)
def test_app_exception_handler_429(monkeypatch):
    """ Tests global 429 handler and ensures limits fall back to local memory safely. """

    monkeypatch.setenv("UPSTASH_REDIS_URL", "memory://")

    from app.rate_limiter import limiter
    limiter.reset()

    hit_triggered_429 = False
    for _ in range(65):
        response = client.get("/")
        if response.status_code == 429:
            hit_triggered_429 = True
            assert response.json()["success"] is False
            assert "Rate limit exceeded" in response.json()["message"]
            break

    assert hit_triggered_429 is True

# Test Exception Handler 2: 404 (app)
def test_app_exception_handler_404():
    """ Tests global 404 Exception Handler for invalid routes. """

    response = client.get("/this-route-does-not-exist")
    assert response.status_code == 404
    assert response.json()["success"] is False
    assert "The requested route does not exist" in response.json()["message"]

# Test Exception Handler 3: 422 (app)
def test_app_exception_handler_422():
    """ Tests global 422 handler by omitting a strictly required body parameter. """

    response = client.post("/v1/language/speech", json={"text": ""})

    assert response.status_code == 422
    assert response.json()["success"] is False
    assert "validation_errors" in response.json()["data"]

# Test Exception Handler 4: 405 (app)
def test_app_exception_handler_405():
    """ Tests global 405 Exception Handler for unsupported HTTP methods on valid routes. """

    response = client.post("/")
    assert response.status_code == 405
    assert response.json()["success"] is False
    assert "is not allowed for this route" in response.json()["message"]

# Test Exception Handler 5: Universal (app)
def test_app_exception_handler_universal(monkeypatch):
    """ Test global 500 handler by forcing a dependency function to raise an unhandled runtime error. """

    local_client = TestClient(app, raise_server_exceptions=False)

    def mock_broken_connection():
        raise RuntimeError("Simulated Database Crash Failure")

    monkeypatch.setattr("app.database.check_connection", mock_broken_connection)

    response = local_client.get("/health")
    assert response.status_code == 500
    assert response.json()["success"] is False
    assert "An internal server error occurred" in response.json()["message"]
    assert response.json()["meta"]["error_type"] == "RuntimeError"