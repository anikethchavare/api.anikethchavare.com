# api.anikethchavare.com - app/database.py

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
from app.config import settings

import asyncio
import logging
from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from pymongo.server_api import ServerApi

# Initializing the Logger
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

# Initializing the Database Client & Collection
database_client = MongoClient(
    settings.mongodb_uri,
    maxPoolSize=2,
    minPoolSize=0,
    maxIdleTimeMS=30000,
    serverSelectionTimeoutMS=3000,
    connectTimeoutMS=5000,
    socketTimeoutMS=5000,
    retryWrites=True,
    w="majority",
    server_api=ServerApi("1")
)

database_collection_request_logs = database_client["api"]["request_logs"]

# Async Function 1: Check Connection
async def check_connection() -> bool:
    """
    Verifies the database health by performing a lightweight ping query.

    Returns:
        True if the database responds successfully, False otherwise.
    """
    
    try:
        await asyncio.to_thread(database_client.admin.command, "ping")
        return True
    except PyMongoError as exception:
        logger.error(f"\nDATABASE ERROR:\nConnection failed: {exception}")
        return False

# Async Function 2: Log Request
async def log_request(
        request_id: str,
        success: bool,
        message: str,
        data: dict,
        meta: dict,
        api_version: str,
        timestamp: datetime,
        status_code: int,
        ip_address: str,
        user_agent: str,
        origin: str,
        path: str,
        vercel_execution_id: str,
        http_version: str,
        error_details: str
) -> None:
    """
    Logs an API request to the "request_logs" database collection in MongoDB (Vercel).

    Args:
        request_id: Unique identifier for the request.
        success: A boolean indicating if the operation was successful.
        message: A human-readable summary of the response or error.
        data: The primary payload.
        meta: Additional context.
        api_version: The version of the API used.
        timestamp: ISO 8601 formatted UTC timestamp.
        status_code: The HTTP status code to return.
        ip_address: The IP address of the client making the request.
        user_agent: The browser or client string identifying the requester.
        origin: The domain that initiated the request.
        path: The specific endpoint path being accessed.
        vercel_execution_id: The unique execution trace ID injected by Vercel.
        http_version: The HTTP protocol version used for the request.
        error_details: Traceback details in case of an error.
    """
    
    document = {
        "_id": request_id,
        "success": success,
        "message": message,
        "data": data,
        "meta": meta,
        "api_version": api_version,
        "timestamp": timestamp,
        "status_code": status_code,
        "ip_address": ip_address,
        "user_agent": user_agent,
        "origin": origin,
        "path": path,
        "vercel_execution_id": vercel_execution_id,
        "http_version": http_version,
        "error_details": error_details
    }
    
    try:
        await asyncio.to_thread(database_collection_request_logs.insert_one, document)
    except PyMongoError as exception:
        logger.error(f"\nDATABASE ERROR:\nAPI request insertion failed: {exception}")