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

# Initializing the Logger (Errors)
logger = logging.getLogger("uvicorn.error")

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

# Function 1: Log Request
def log_request(
        request_id: str,
        success: bool,
        message: str,
        data: dict,
        meta: dict,
        api_version: str,
        timestamp: str,
        status_code: int
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

    Returns:
        This function performs an asynchronous-style write and returns nothing.

    Raises:
        psycopg2.Error: If the database connection fails or the query is invalid.
    """

    connection = None

    try:
        # Connecting to the Database
        connection = connection_pool.getconn()
        connection.autocommit = True
        cursor = connection.cursor()

        # Create Table if Not Exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS request_logs (
                request_id TEXT PRIMARY KEY,
                success BOOLEAN,
                message TEXT,
                data JSONB,
                meta JSONB,
                api_version TEXT,
                timestamp TIMESTAMP WITH TIME ZONE,
                status_code INTEGER
            );
        """)

        # Insert Data into the "request_logs" Table
        query = """
            INSERT INTO request_logs (
                request_id, success, message, data, meta,
                api_version, timestamp, status_code
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """

        cursor.execute(query, (
            request_id,
            success,
            message,
            json.dumps(data),
            json.dumps(meta),
            api_version,
            timestamp,
            status_code
        ))

        # Closing the Cursor
        cursor.close()
    except Exception as log_request_exception:
        logger.error(f"DATABASE ERROR:\n{log_request_exception}")
    finally:
        if connection:
            connection_pool.putconn(connection)