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
import psycopg2
from dotenv import load_dotenv

# Loading Environment Variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

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

    # Initializing the "request_logs" Database
    connection = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()

    connection.autocommit = True

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

    # Insert Data into the "request_logs" Database
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

    # Closing the Connection
    cursor.close()
    connection.close()