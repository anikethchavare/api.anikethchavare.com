# api.anikethchavare.com - routers/app_v1.py

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
from app import utils
from app import rate_limiter

from fastapi import APIRouter, Request

# Initializing the "router_app_v1" API Router
router_app_v1 = APIRouter(prefix="/v1")

# Route 1: main (router_app_v1)
@router_app_v1.get("/")
@rate_limiter.limiter.limit("60/minute")
async def router_app_v1_main(request: Request):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Welcome to Version 1 of the API."
    )