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

import uuid
from typing import Any, Dict, Optional
from datetime import datetime, timezone

from fastapi import Request
from fastapi.responses import JSONResponse

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
    metadata such as unique request IDs and UTC timestamps.

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

    # Initialize Base Meta
    base_meta = {"rate_limit": "60 requests per minute."}

    # Initialize Fresh Dictionaries for "data" and "meta" if None
    if data is None:
        data = {}
    if meta is None:
        meta = {}

    # Merge Additional Meta Info
    if meta:
        base_meta.update(meta)

    # Creating the APIResponse Model
    response = schemas.APIResponse(
        success=success,
        message=message,
        data=data,
        meta=base_meta,
        api_version=schemas.API_VERSION,
        timestamp=datetime.now(timezone.utc).isoformat(),
        request_id=f"req_{uuid.uuid4()}",
        status_code=status_code
    )

    return JSONResponse(content=response.model_dump())