# api.anikethchavare.com - tests/routers/test_app_v1.py

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
from fastapi.testclient import TestClient

# Initializing the TestClient
client = TestClient(app)

# Test Route 1: Main (app_v1)
def test_app_v1_main():
    """ Tests the API Version 1 root entrance gateway (GET /v1/). """

    response = client.get("/v1/")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "Welcome to Version 1 of the API." in response.json()["message"]
    assert "1_core.md" in response.json()["meta"]["docs"]