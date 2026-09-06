# api.anikethchavare.com - routers/v1/ghost_protocol.py

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
from app.config import settings

import logging
from ably import AblyRest
from pydantic import StrictStr

from fastapi import APIRouter, Request, BackgroundTasks, Body

# Initializing the "app_v1_ghost_protocol" API Router
app_v1_ghost_protocol = APIRouter(prefix="/ghost-protocol")

# Initializing the Logger (Errors)
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

# Ably Client Initialization
ably_client = AblyRest(settings.ably_api_key)

# Route 1: Main (app_v1_ghost_protocol)
@app_v1_ghost_protocol.get("/")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_ghost_protocol_main(request: Request, background_tasks: BackgroundTasks):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Welcome to the 'ghost-protocol' utility namespace. Check the documentation for available endpoints.",
        background_tasks=background_tasks,
        meta={
            "help": "Check the API v1 documentation (/ghost-protocol) for available endpoints.",
            "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs/v1/5_ghost_protocol.md"
        }
    )

# Route 2: Generate Token (app_v1_ghost_protocol)
@app_v1_ghost_protocol.get("/generate-token")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_ghost_protocol_generate_token(
        request: Request,
        background_tasks: BackgroundTasks,
        client_id: StrictStr = Body(..., embed=True, description="The client ID."),
        room_id: StrictStr = Body(..., embed=True, description="The room ID."),
        username: StrictStr = Body(..., embed=True, description="The member's username."),
        action: StrictStr = Body(..., embed=True, description="The choice to 'create' or 'join' a room.")
):
    # Establishing Channel Reference
    channel = ably_client.channels.get(f"room:{room_id}")
    
    # Fetching "Presence" Data
    try:
        presence_page = await channel.presence.get()
        presence_members = presence_page.items
    except Exception as e:
        logger.error(f"ABLY INTERNAL ERROR: Failed to fetch presence data: {e}")
        
        return utils.send_response(
            request=request,
            status_code=500,
            success=False,
            message="Failed to validate room metadata status.",
            background_tasks=background_tasks
        )
    
    # Validation: Checking if Room Exists
    if action.lower() == "join" and not presence_members:
        return utils.send_response(
            request=request,
            status_code=404,
            success=False,
            message="The room ID does not exist or is inactive.",
            background_tasks=background_tasks
        )
    
    # Validation: Checking if Username is Taken
    if any(member.data == username.strip().replace(" ", "-") for member in presence_members):
        return utils.send_response(
            request=request,
            status_code=409,
            success=False,
            message="The username is already taken by another active member.",
            background_tasks=background_tasks
        )
    
    # Assembling "token_request"
    token_request = await ably_client.auth.create_token_request({
        "client_id": client_id,
        "capability": {
            f"room:{room_id}": ["publish", "subscribe", "presence", "channel-metadata"]
        }
    })
    
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Successfully generated the Ably token.",
        background_tasks=background_tasks,
        data=token_request.to_dict()
    )