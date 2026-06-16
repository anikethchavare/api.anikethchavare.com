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
import psycopg2
from psycopg2 import pool
from dotenv import load_dotenv
from typing import Any, Callable

# Initializing the Logger
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

# Loading Environment Variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Initializing the Connection Pool
try:
    connection_pool = psycopg2.pool.SimpleConnectionPool(
        1,
        10,
        dsn=DATABASE_URL
    )
except Exception as connection_pool_exception:
    logger.error(f"DATABASE ERROR:\n{connection_pool_exception}")

# Handler Function 1: Handle DB Exception
def _handle_db_exception(
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

    if isinstance(exception, (psycopg2.OperationalError, psycopg2.InterfaceError)):
        if retry_count < 1:
            logger.warning(f"DATABASE WARNING:\nConnection lost. Retrying... (Error: {exception})")

            if connection:
                connection_pool.putconn(connection, close=True)

            kwargs["retry_count"] = retry_count + 1
            return retry_func(*args, **kwargs)
        else:
            logger.error(f"DATABASE ERROR:\nConnection retry failed. Dropping operation: {retry_func.__name__}")
            return False
    else:
        logger.error(f"DATABASE ERROR:\n{exception}")
        return False

# Function 1: Initialize Database
def init_db(retry_count: int = 0) -> None:
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
        connection = connection_pool.getconn()
        connection.autocommit = True
        cursor = connection.cursor()

        # Create Table: request_logs
        cursor.execute("""
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
                    http_version TEXT
                );
            """)

        # Closing the Cursor
        cursor.close()
    except Exception as db_exception:
        return _handle_db_exception(db_exception, connection, init_db, retry_count=retry_count)
    finally:
        if connection:
            connection_pool.putconn(connection)

# Function 2: Check Connection
def check_connection(retry_count: int = 0) -> bool:
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
        connection = connection_pool.getconn()
        connection.autocommit = True
        cursor = connection.cursor()

        # Executing a Simple Ping Query
        cursor.execute("SELECT 1;")
        cursor.fetchone()

        # Closing the Cursor
        cursor.close()
        return True
    except Exception as db_exception:
        return _handle_db_exception(db_exception, connection, check_connection, retry_count=retry_count)
    finally:
        if connection:
            connection_pool.putconn(connection)

# Function 3: Log Request
def log_request(
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
        retry_count: The number of times to retry the request.

    Returns:
        None (Logs warnings and errors to the logger).
    """

    connection = None
    local_args = locals()
    del local_args["connection"]

    try:
        # Fetching a Connection from the Pool
        connection = connection_pool.getconn()
        connection.autocommit = True
        cursor = connection.cursor()

        # Insert Data into the "request_logs" Table
        query = """
            INSERT INTO request_logs (
                request_id, success, message, data, meta,
                api_version, timestamp, status_code, ip_address, user_agent,
                origin, path, vercel_execution_id, http_version
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        cursor.execute(query, (
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
            http_version
        ))

        # Closing the Cursor
        cursor.close()
    except Exception as db_exception:
        return _handle_db_exception(db_exception, connection, log_request, **local_args)
    finally:
        if connection:
            connection_pool.putconn(connection)