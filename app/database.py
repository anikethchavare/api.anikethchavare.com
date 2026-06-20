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
import os
import json
import logging

import psycopg
from dotenv import load_dotenv
from typing import Any, Callable, Optional
from psycopg_pool import AsyncConnectionPool

# Initializing the Logger
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

# Loading Environment Variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Initializing the Connection Pool
connection_pool: Optional[AsyncConnectionPool] = None

# Function 1: Initialize Connection Pool
async def init_pool():
    """
    Initializes the database connection pool asynchronously at server startup.
    """

    global connection_pool

    try:
        connection_pool = AsyncConnectionPool(
            conninfo=DATABASE_URL,
            min_size=1,
            max_size=2,
            open=False,
            kwargs={"autocommit": True}
        )

        await connection_pool.open()
    except Exception as connection_pool_exception:
        logger.error(f"\nDATABASE ERROR:\n{connection_pool_exception}")
        raise RuntimeError(f"DATABASE ERROR: {connection_pool_exception}")

# Function 2: Close Connection Pool
async def close_pool():
    """
    Closes the database connection pool.
    """

    global connection_pool

    if connection_pool:
        await connection_pool.close()

# Handler Function 1: Handle DB Exception
async def _handle_db_exception(
        exception: Exception,
        connection: Any,
        retry_func: Callable[..., Any],
        *args: Any,
        **kwargs: Any
) -> Any:
    """
    Centralized handler for database exceptions.

    Args:
        exception: The database exception to handle.
        connection: The database connection.
        retry_func: Function to be retried.
        *args: Arguments to be passed.
        **kwargs: Keyword arguments to be passed.

    Returns:
        Any (Object of any data type).
    """

    retry_count = kwargs.get("retry_count", 0)

    if isinstance(exception, (psycopg.OperationalError, psycopg.InterfaceError)):
        if retry_count < 1:
            logger.warning(f"\nDATABASE WARNING:\nConnection lost. Retrying... (Error: {exception})")

            if connection and connection_pool:
                await connection_pool.putconn(connection)

            kwargs["retry_count"] = retry_count + 1
            return await retry_func(*args, **kwargs)
        else:
            logger.error(f"\nDATABASE ERROR:\nConnection retry failed. Dropping operation: {retry_func.__name__}")
            return False
    else:
        logger.error(f"\nDATABASE ERROR:\n{exception}")
        return False

# Function 3: Initialize Database
async def init_db(retry_count: int = 0) -> None:
    """
    Initializes the core database by ensuring all required tables exist.

    Args:
        retry_count: The number of times to retry the request.

    Returns:
        None (Logs warnings and errors to the logger).
    """

    connection = None

    try:
        # Fetching a Connection from the Pool
        connection = await connection_pool.getconn()

        # Create Table: request_logs
        async with connection.cursor() as cursor:
            await cursor.execute("""
                    CREATE TABLE IF NOT EXISTS request_logs (
                        request_id TEXT PRIMARY KEY,
                        success BOOLEAN,
                        message TEXT,
                        data JSONB,
                        meta JSONB,
                        api_version TEXT,
                        timestamp TIMESTAMP WITH TIME ZONE,
                        status_code INTEGER,
                        ip_address TEXT,
                        user_agent TEXT,
                        origin TEXT,
                        path TEXT,
                        vercel_execution_id TEXT,
                        http_version TEXT,
                        error_details TEXT
                    );
                """)
    except Exception as db_exception:
        return await _handle_db_exception(db_exception, connection, init_db, retry_count=retry_count)
    finally:
        if connection:
            await connection_pool.putconn(connection)

# Function 4: Check Connection
async def check_connection(retry_count: int = 0) -> bool:
    """
    Verifies the database health by performing a lightweight ping query.

    Args:
        retry_count: The number of times to retry the request.

    Returns:
        True if the database responds successfully, False otherwise.
    """

    connection = None

    try:
        # Fetching a Connection from the Pool
        connection = await connection_pool.getconn()

        # Executing a Simple Ping Query
        async with connection.cursor() as cursor:
            await cursor.execute("SELECT 1;")
            await cursor.fetchone()

        return True
    except Exception as db_exception:
        return await _handle_db_exception(db_exception, connection, check_connection, retry_count=retry_count)
    finally:
        if connection:
            await connection_pool.putconn(connection)

# Function 5: Log Request
async def log_request(
        request_id: str,
        success: bool,
        message: str,
        data: dict,
        meta: dict,
        api_version: str,
        timestamp: str,
        status_code: int,
        ip_address: str,
        user_agent: str,
        origin: str,
        path: str,
        vercel_execution_id: str,
        http_version: str,
        error_details: str,
        retry_count: int = 0
) -> None:
    """
    Logs an API request to the "request_logs" database table in Neon (Vercel).

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
        retry_count: The number of times to retry the request.

    Returns:
        None (Logs warnings and errors to the logger).
    """

    connection = None
    local_args = locals()
    del local_args["connection"]

    try:
        # Fetching a Connection from the Pool
        connection = await connection_pool.getconn()

        # Insert Data into the "request_logs" Table
        async with connection.cursor() as cursor:
            await cursor.execute("""
                INSERT INTO request_logs (
                    request_id, success, message, data, meta,
                    api_version, timestamp, status_code, ip_address, user_agent,
                    origin, path, vercel_execution_id, http_version, error_details
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """, (
                request_id,
                success,
                message,
                json.dumps(data),
                json.dumps(meta),
                api_version,
                timestamp,
                status_code,
                ip_address,
                user_agent,
                origin,
                path,
                vercel_execution_id,
                http_version,
                error_details
            ))
    except Exception as db_exception:
        return await _handle_db_exception(db_exception, connection, log_request, **local_args)
    finally:
        if connection:
            await connection_pool.putconn(connection)