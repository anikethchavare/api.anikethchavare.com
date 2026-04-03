# api.anikethchavare.com - server.py

"""
Copyright 2026 Aniketh Chavare (anikethchavare@zohomail.in)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# Imports
from schema import API_VERSION, APIResponse

import time
import uuid
from typing import Any, Dict, Optional
from fastapi import FastAPI, Request
from datetime import datetime, timezone
from fastapi.responses import JSONResponse

"""
Response Structure: All API responses must follow this order:

1. success - Boolean, true if the request succeeded, false otherwise.
2. message - Human-readable message for success, or structured error object for failures.
3. data - Payload of the response (if any).
4. meta - Contextual metadata including rate limit thresholds, remaining quota, and reset timestamps.
5. api_version - API version string.
6. timestamp - UTC timestamp of the response.
7. request_id - Unique identifier (prefix req_) for trace logging and server-side debugging.
8. response_time_ms - Server-side execution latency measured in milliseconds.
9. status_code - HTTP status code for the response.
"""

# Initializing the "app" FastAPI Server
app = FastAPI(docs_url=None, redoc_url=None)

# Middleware 1: Timer for "response_time_ms"
@app.middleware("http")
async def add_timer(request: Request, call_next):
    start_time = time.perf_counter()

    response = await call_next(request)

    process_time = round((time.perf_counter() - start_time) * 1000, 2)
    request.state.process_time = process_time

    return response

# Function 1: Send Response
def send_response(
    request: Request,
    status_code: int,
    success: bool,
    message: str,
    data: Optional[Dict[str, Any]] = None,
    meta: Optional[Dict[str, Any]] = None
):
    """
    Constructs and returns a standardized API response.

    This helper function ensures all API endpoints follow the unified response
    contract defined in the APIResponse schema. It automatically injects
    metadata such as unique request IDs, UTC timestamps, and the execution
    time measured by the middleware.

    Args:
        request: The incoming FastAPI request object used to retrieve state
            information like processing time.
        status_code: The HTTP status code to return.
        success: A boolean indicating if the operation was successful.
        message: A human-readable summary of the response or error.
        data: The primary payload. If None, an empty dict is initialized.
        meta: Additional context. If None, an empty dict is initialized.

    Returns:
        A FastAPI JSONResponse object containing the serialized APIResponse
        model and the specified HTTP status code.
    """

    # Initialize Fresh Dictionaries for "data" and "meta" if None
    if data is None:
        data = {}
    if meta is None:
        meta = {}

    # Creating the APIResponse Model
    response = APIResponse(
        success=success,
        message=message,
        data=data,
        meta=meta,
        api_version=API_VERSION,
        timestamp=datetime.now(timezone.utc).isoformat(),
        request_id=f"req_{uuid.uuid4()}",
        response_time_ms=getattr(request.state, "process_time", 0),
        status_code=status_code
    )

    return JSONResponse(content=response.model_dump())

# Route 1: main (app)
@app.get("/")
async def app_main(request: Request):
    return send_response(
        request=request,
        status_code=200,
        success=True,
        message="A public API powered by FastAPI and Python, deployed to Vercel."
    )