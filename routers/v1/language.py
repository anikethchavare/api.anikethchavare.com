# api.anikethchavare.com - routers/v1/language.py

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
from pydantic import StrictStr, StrictBool

from fastapi import APIRouter, Request, BackgroundTasks, Query

# Initializing the "app_v1_language" API Router
app_v1_language = APIRouter(prefix="/language")

# Route 1: Main (app_v1_language)
@app_v1_language.get("/")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_language_main(request: Request, background_tasks: BackgroundTasks):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Welcome to the 'language' utility namespace. Check the documentation for available endpoints.",
        background_tasks=background_tasks,
        meta={
            "help": "Check the API v1 documentation (/language) for available endpoints.",
            "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs/v1/2_language.md"
        }
    )

# Route 2: Dictionary (app_v1_language)
@app_v1_language.get("/dictionary")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_language_dictionary(
        request: Request,
        background_tasks: BackgroundTasks,
        word: StrictStr = Query(..., min_length=1),
        phonetics: StrictBool = Query(True, description="If true, outputs 'phonetics'."),
        definitions: StrictBool = Query(True, description="If true, outputs the entire 'definitions' list."),
        strict: StrictBool = Query(False, description="Modifies 'definitions' to output a flat list of strings. Only applies if 'definitions=true'.")
):
    # Fetching Data & Assembling 'payload'
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

    if response.status_code == 404:
        return utils.send_response(
            request=request,
            status_code=404,
            success=False,
            message=f"No data was found for the word '{word}'.",
            background_tasks=background_tasks
        )
    elif response.status_code != 200:
        return utils.send_response(
            request=request,
            status_code=502,
            success=False,
            message="An unexpected error occurred while querying the dictionary. Please try again later.",
            background_tasks=background_tasks
        )

    response_data = orjson.loads(response.content)[0]

    payload = {
        "word": response_data.get("word", word),
        "phonetics": response_data["phonetics"] if phonetics else None,
        "definitions": None,
        "license": response_data.get("license"),
        "source_urls": response_data.get("sourceUrls")
    }

    if definitions:
        if strict:
            meanings = [
                sub["definition"]
                for meaning in response_data["meanings"]
                for sub in meaning["definitions"]
            ]
        else:
            meanings = [
                {
                    "part_of_speech": meaning["partOfSpeech"],
                    "definitions": [sub["definition"] for sub in meaning["definitions"]]
                }
                for meaning in response_data["meanings"]
            ]

        payload["definitions"] = meanings
    else:
        payload["definitions"] = None

    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Successfully queried the dictionary for the word.",
        background_tasks=background_tasks,
        data=payload
    )