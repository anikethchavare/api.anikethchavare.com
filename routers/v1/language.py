# api.anikethchavare.com - routers/v1/language.py

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

from fastapi import APIRouter, Request, BackgroundTasks

# Initializing the "app_v1_language" API Router
app_v1_language = APIRouter(prefix="/language")

# Route 1: main (app_v1_language)
@app_v1_language.get("/")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_language_main(request: Request, background_tasks: BackgroundTasks):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Welcome to the 'language' utility namespace. Check the documentation for available endpoints.",
        background_tasks=background_tasks,
        meta={
            "help": "Check the API v1 documentation for available endpoints.",
            "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs/v1/2_language.md"
        }
    )