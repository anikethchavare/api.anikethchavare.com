# api.anikethchavare.com - app/utils.py

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
from app import schemas
from app import database

from typing import Any, Dict, Optional

from fastapi.responses import JSONResponse
from fastapi import Request, BackgroundTasks

# Function 1: Send Response
def send_response(
    request: Request,
    status_code: int,
    success: bool,
    message: str,
    background_tasks: BackgroundTasks,
    data: Optional[Dict[str, Any]] = None,
    meta: Optional[Dict[str, Any]] = None,
    error_details: str = None
) -> JSONResponse:
    """
    Constructs and returns a standardized API response. Also, logs the request
    to the Neon (Vercel) database.

    This helper function ensures all API endpoints follow the unified response
    contract defined in the APIResponse schema. It automatically injects
    metadata such as unique request IDs and UTC timestamps.

    Args:
        request: The incoming FastAPI request object used to retrieve state
            information like processing time.
        status_code: The HTTP status code to return.
        success: A boolean indicating if the operation was successful.
        message: A human-readable summary of the response or error.
        background_tasks: An instance of FastAPI's "BackgroundTasks".
        data: The primary payload. If None, an empty dict is initialized.
        meta: Additional context. If None, an empty dict is initialized.
        error_details: Traceback details in case of an error.

    Returns:
        A FastAPI JSONResponse object containing the serialized APIResponse
        model and the specified HTTP status code.
    """

    # Initialize Base Meta
    base_meta = {"rate_limit": "60 requests per minute."}

    # Initialize Fresh Dictionaries for "data" and "meta" if None
    if data is None: data = {}
    if meta is None: meta = {}
    if meta: base_meta.update(meta)

    # Defining Response Dictionary
    response_args = {
        "success": success,
        "message": message,
        "data": data,
        "meta": base_meta,
        "api_version": schemas.API_VERSION,
        "timestamp": request.state.timestamp,
        "request_id": request.state.request_id,
        "status_code": status_code,
        "error_details": error_details,
        **request.state.telemetry_data
    }

    # Creating the APIResponse Model
    response = schemas.APIResponse(**response_args)

    # Logging the Request
    background_tasks.add_task(database.log_request, **response_args)

    json_response = JSONResponse(content=response.model_dump(), status_code=status_code)
    json_response.background = background_tasks

    return json_response