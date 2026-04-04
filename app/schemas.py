# api.anikethchavare.com - app/schemas.py

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
from typing import Any, Dict
from pydantic import BaseModel

# Constants
API_VERSION = "0.6.0"

# Class 1 - API Response
class APIResponse(BaseModel):
    success: bool
    message: str
    data: Dict[str, Any] = {}
    meta: Dict[str, Any] = {}
    api_version: str
    timestamp: str
    request_id: str
    status_code: int