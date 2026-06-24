# api.anikethchavare.com - routers/v1/entertainment.py

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

import httpx
import orjson
from typing import Literal
from pydantic import StrictInt, StrictStr

from fastapi import APIRouter, Request, BackgroundTasks, Query

# Initializing the "app_v1_entertainment" API Router
app_v1_entertainment = APIRouter(prefix="/entertainment")

# Route 1: Main (app_v1_entertainment)
@app_v1_entertainment.get("/")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_entertainment_main(request: Request, background_tasks: BackgroundTasks):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Welcome to the 'entertainment' utility namespace. Check the documentation for available endpoints.",
        background_tasks=background_tasks,
        meta={
            "help": "Check the API v1 documentation (/entertainment) for available endpoints.",
            "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs/v1/4_entertainment.md"
        }
    )

# Route 2: Jokes (app_v1_entertainment)
@app_v1_entertainment.get("/jokes")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_entertainment_jokes(
        request: Request,
        background_tasks: BackgroundTasks,
        category: StrictStr = Query("Any", description="The category of the joke."),
        type: Literal["single", "twopart"] | None = Query(None, description="The type of joke."),
        blacklist: StrictStr | None = Query(None, description="The jokes with these flags will not be served."),
        amount: StrictInt = Query(1, ge=1, le=10, description="The amount of jokes to serve in a single request.")
):
    allowed_categories = ("Any", "Programming", "Misc", "Dark", "Pun", "Spooky", "Christmas")
    allowed_blacklists = ("nsfw", "religious", "political", "racist", "sexist", "explicit")

    requested_categories = [cat.strip() for cat in category.split(",")]
    requested_blacklists = []

    for cat in requested_categories:
        if cat not in allowed_categories:
            return utils.send_response(
                request=request,
                status_code=422,
                success=False,
                message=f"Validation Error: '{cat}' is not a valid category. Choose from {list(allowed_categories)}.",
                background_tasks=background_tasks
            )

    if blacklist:
        requested_blacklists = [flag.strip() for flag in blacklist.split(",")]

        for flag in requested_blacklists:
            if flag not in allowed_blacklists:
                return utils.send_response(
                    request=request,
                    status_code=422,
                    success=False,
                    message=f"Validation Error: '{flag}' is not a valid flag. Choose from {list(allowed_blacklists)}.",
                    background_tasks=background_tasks
                )

    # Assembling Query Parameters
    query_params = {
        "amount": amount,
    }

    if type:
        query_params["type"] = type
    if requested_blacklists:
        query_params["blacklistFlags"] = ",".join(requested_blacklists)

    # Fetching Data & Assembling 'jokes_list'
    async with httpx.AsyncClient() as client:
        response = await client.get(
        f"https://v2.jokeapi.dev/joke/{','.join(requested_categories)}",
            params=query_params
        )

    if response.status_code != 200:
        return utils.send_response(
            request=request,
            status_code=502,
            success=False,
            message="An unexpected error occurred while fetching jokes. Please try again later.",
            background_tasks=background_tasks
        )

    response_data = orjson.loads(response.content)

    if response_data.get("error") is True:
        return utils.send_response(
            request=request,
            status_code=400,
            success=False,
            message=f"JokeAPI Error: {response_data.get('additionalInfo', 'Invalid request parameters.')}",
            background_tasks=background_tasks
        )

    jokes_list = []

    for joke_item in response_data.get("jokes", [response_data]):
        if joke_item.get("type") == "single":
            jokes_list.append(joke_item["joke"])
        else:
            jokes_list.append((joke_item["setup"], joke_item["delivery"]))

    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Successfully fetched the jokes.",
        background_tasks=background_tasks,
        data={
            "jokes": jokes_list,
            "safe": response_data.get("jokes", [response_data])[0].get("safe", True)
        }
    )