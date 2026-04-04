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

import os
import logging
import traceback

from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, HTTPException

from slowapi import Limiter
from slowapi.util import get_remote_address
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

# Initializing the "app" FastAPI Server
app = FastAPI(docs_url=None, redoc_url=None)

# Initializing the Rate Limiter
limiter = Limiter(key_func=get_remote_address, default_limits=["60/minute"])
app.state.limiter = limiter

# Initializing the Logger (Errors)
logger = logging.getLogger("uvicorn.error")

# Configure CORS for Secure Public Access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware 1: Security Headers
@app.middleware("http")
async def middleware_security_headers(request: Request, call_next):
    response = await call_next(request)

    response.headers["X-XSS-Protection"] = "0"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-API-VERSION"] = schemas.API_VERSION
    response.headers["Permissions-Policy"] = "geolocation=(), camera=(), microphone=()"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Content-Security-Policy"] = "default-src 'none'; frame-ancestors 'none'; sandbox"

    return response

# Route 1: main (app)
@app.get("/")
@limiter.limit("60/minute")
async def app_main(request: Request):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="A public API powered by FastAPI and Python, deployed to Vercel."
    )

# Route 2: favicon.ico (app)
@app.get("/favicon.ico")
@limiter.limit("60/minute")
async def app_favicon(request: Request):
    return FileResponse(
        os.getcwd().replace(os.sep, "/") + "/media/favicon.png",
        status_code=200
    )

# Exception Handler 1: Rate Limiting
@app.exception_handler(RateLimitExceeded)
async def exception_handler_rate_limiting(request: Request, exc: RateLimitExceeded):
    return utils.send_response(
        request=request,
        status_code=429,
        success=False,
        message="Rate limit exceeded. Please try again later."
    )

# Exception Handler 2: Error 404
@app.exception_handler(404)
async def exception_handler_error_404(request: Request, exec: HTTPException):
    return utils.send_response(
        request=request,
        status_code=404,
        success=False,
        message="The requested route does not exist."
    )

# Exception Handler 3: Universal
@app.exception_handler(Exception)
async def exception_handler_universal(request: Request, exc: Exception):
    error_details = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
    logger.error(f"INTERNAL SERVER ERROR on {request.url.path}:\n{error_details}")

    return utils.send_response(
        request=request,
        status_code=500,
        success=False,
        message="An internal server error occurred.",
        meta={
            "error_type": type(exc).__name__,
            "path": request.url.path,
            "report_issue": "https://github.com/anikethchavare/api.anikethchavare.com/issues",
            "help": "If this persists, please open an issue with the error_type, request_id, and timestamp."
        }
    )

# Adding Exception Handler 1
app.add_exception_handler(RateLimitExceeded, exception_handler_rate_limiting)