# api.anikethchavare.com - server.py

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
from app import schemas
from app import database
from app import rate_limiter

from routers.app_v1 import router_app_v1

import os
import uuid
import logging
import traceback
from datetime import datetime, timezone
from contextlib import asynccontextmanager

from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, HTTPException, BackgroundTasks

from slowapi.errors import RateLimitExceeded

"""
Response Structure: All API responses must follow this order:

1. success - Boolean, true if the request succeeded, false otherwise.
2. message - Human-readable message for success, or structured error object for failures.
3. data - Payload of the response (if any).
4. meta - Contextual metadata including rate limit thresholds, remaining quota, and reset timestamps.
5. api_version - API version string.
6. timestamp - UTC timestamp of the response.
7. request_id - Unique identifier (prefix req_) for trace logging and server-side debugging.
8. status_code - HTTP status code for the response.
"""

# Async Context Manager: Lifespan
@asynccontextmanager
async def async_context_manager_lifespan(app_local: FastAPI):
    # Startup: Initialize the Async Connection Pool and Database
    await database.init_pool()
    await database.init_db()
    yield

    # Shutdown: Close the Async connection pool.
    await database.close_pool()

# Initializing the "app" FastAPI Server
app = FastAPI(title="api.anikethchavare.com",
              description="A high-performance, general-purpose public REST API powered by FastAPI and Python.",
              version=schemas.API_VERSION,
              license_info={
                  "name": "Apache 2.0",
                  "url": "https://www.apache.org/licenses/LICENSE-2.0"
              },
              docs_url=None,
              redoc_url=None,
              lifespan=async_context_manager_lifespan)

app.state.limiter = rate_limiter.limiter

# Initializing the Logger (Errors)
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

# Configure CORS for Secure Public Access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global Security Headers
SECURITY_HEADERS = {
    "X-XSS-Protection": "0",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "no-referrer",
    "X-Content-Type-Options": "nosniff",
    "X-API-VERSION": schemas.API_VERSION,
    "Permissions-Policy": "geolocation=(), camera=(), microphone=()",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
    "Content-Security-Policy": "default-src 'none'; frame-ancestors 'none'; sandbox"
}

# Middleware 1: Security Headers (app)
@app.middleware("http")
async def middleware_security_headers(request: Request, call_next):
    response = await call_next(request)

    response.headers.update(SECURITY_HEADERS)

    return response

# Middleware 2: Telemetry Pre-Calculation (app)
@app.middleware("http")
async def middleware_telemetry_pre_calculation(request: Request, call_next):
    request.state.request_id = f"req_{uuid.uuid4()}"
    request.state.timestamp = datetime.now(timezone.utc).isoformat()

    request.state.telemetry_data = {
        "ip_address": request.client.host if request.client else "unknown",
        "user_agent": request.headers.get("user-agent"),
        "origin": request.headers.get("origin") or "direct",
        "path": request.url.path,
        "vercel_execution_id": request.headers.get("X-Vercel-Id"),
        "http_version": request.scope.get("http_version")
    }

    return await call_next(request)

# Include the API Routers
app.include_router(router_app_v1)

# Route 1: main (app)
@app.get("/")
@rate_limiter.limiter.limit("60/minute")
async def app_main(request: Request, background_tasks: BackgroundTasks):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="A high-performance, general-purpose public REST API powered by FastAPI and Python.",
        background_tasks=background_tasks
    )

# Route 2: favicon.ico (app)
@app.get("/favicon.ico", include_in_schema=False)
@rate_limiter.limiter.limit("60/minute")
async def app_favicon(request: Request):
    return FileResponse(
        os.getcwd().replace(os.sep, "/") + "/media/favicon.png",
        status_code=200
    )

# Route 3: health (app)
@app.get("/health", include_in_schema=False)
async def app_health(request: Request, background_tasks: BackgroundTasks):
    # Performing Health Checks
    api_working = True if app.router.routes else False
    db_working = await database.check_connection()

    health_data = {
        "api": "pass" if api_working else "fail",
        "database": "pass" if db_working else "fail"
    }

    healthy = all(value == "pass" for value in health_data.values())

    return utils.send_response(
        request=request,
        status_code=200 if healthy else 503,
        success=healthy,
        message="API is healthy and running." if healthy else "API is unhealthy and non-responsive. One or more internal services are currently unavailable.",
        background_tasks=background_tasks,
        data={"health_checks": health_data}
    )

# Exception Handler 1: Rate Limiting (app)
@app.exception_handler(RateLimitExceeded)
async def exception_handler_rate_limiting(request: Request, exc: RateLimitExceeded):
    return utils.send_response(
        request=request,
        status_code=429,
        success=False,
        message="Rate limit exceeded. Please try again later.",
        background_tasks=BackgroundTasks()
    )

# Exception Handler 2: Error 404 (app)
@app.exception_handler(404)
async def exception_handler_error_404(request: Request, exec: HTTPException):
    return utils.send_response(
        request=request,
        status_code=404,
        success=False,
        message="The requested route does not exist.",
        background_tasks=BackgroundTasks(),
        meta={
            "path": request.url.path,
            "help": "Check the API documentation for valid endpoints.",
            "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs"
        }
    )

# Exception Handler 3: Universal (app)
@app.exception_handler(Exception)
async def exception_handler_universal(request: Request, exc: Exception):
    error_details = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
    logger.error(f"INTERNAL SERVER ERROR on {request.url.path}:\n{error_details}")

    return utils.send_response(
        request=request,
        status_code=500,
        success=False,
        message="An internal server error occurred. Please try again later.",
        background_tasks=BackgroundTasks(),
        meta={
            "error_type": type(exc).__name__,
            "path": request.url.path,
            "report_issue": "https://github.com/anikethchavare/api.anikethchavare.com/issues",
            "help": "If this persists, please open an issue with the request_id."
        }
    )