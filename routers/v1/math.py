# api.anikethchavare.com - routers/v1/math.py

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

import math
import statistics
from pydantic import Field
from typing import Union, Literal, List, Annotated

from fastapi import APIRouter, Request, BackgroundTasks, Query, Body

# Initializing the "app_v1_math" API Router
app_v1_math = APIRouter(prefix="/math")

# Route 1: Main (app_v1_math)
@app_v1_math.get("/")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_main(request: Request, background_tasks: BackgroundTasks):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Welcome to the 'math' utility namespace. Check the documentation for available endpoints.",
        background_tasks=background_tasks,
        meta={
            "help": "Check the API v1 documentation (/math) for available endpoints.",
            "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs/v1/3_math.md"
        }
    )

# Route 2: Trigonometry (app_v1_math)
@app_v1_math.get("/trigonometry")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_trigonometry(request: Request, background_tasks: BackgroundTasks):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Welcome to the 'trigonometry' sub-utility namespace under 'math'. Check the documentation for available endpoints.",
        background_tasks=background_tasks,
        meta={
            "help": "Check the API v1 documentation (/math) for available endpoints.",
            "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs/v1/3_math.md"
        }
    )

# Route 3: Trigonometry - Degrees to Radians (app_v1_math)
@app_v1_math.get("/trigonometry/degrees-to-radians")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_trigonometry_degrees_to_radians(
        request: Request,
        background_tasks: BackgroundTasks,
        degrees: Union[int, float] = Query(..., description="The value of degrees to convert to radians.")
):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Successfully converted degrees to radians.",
        background_tasks=background_tasks,
        data={
            "radians": math.radians(degrees)
        }
    )

# Route 4: Trigonometry - Radians to Degrees (app_v1_math)
@app_v1_math.get("/trigonometry/radians-to-degrees")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_trigonometry_radians_to_degrees(
        request: Request,
        background_tasks: BackgroundTasks,
        radians: Union[int, float] = Query(..., description="The value of radians to convert to degrees.")
):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Successfully converted radians to degrees.",
        background_tasks=background_tasks,
        data={
            "degrees": math.degrees(radians)
        }
    )

# Route 5: Trigonometry - Sin (app_v1_math)
@app_v1_math.get("/trigonometry/sin")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_trigonometry_sin(
        request: Request,
        background_tasks: BackgroundTasks,
        value: Union[int, float] = Query(..., description="The value of degrees or radians to convert to sin."),
        unit: Literal["degrees", "radians"] = Query(..., description="The unit of the value provided.")
):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message=f"Successfully converted the value from {unit} to sin.",
        background_tasks=background_tasks,
        data={
            "result": math.sin(math.radians(value) if unit == "degrees" else value)
        }
    )

# Route 6: Trigonometry - Cos (app_v1_math)
@app_v1_math.get("/trigonometry/cos")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_trigonometry_cos(
        request: Request,
        background_tasks: BackgroundTasks,
        value: Union[int, float] = Query(..., description="The value of degrees or radians to convert to cos."),
        unit: Literal["degrees", "radians"] = Query(..., description="The unit of the value provided.")
):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message=f"Successfully converted the value from {unit} to cos.",
        background_tasks=background_tasks,
        data={
            "result": math.cos(math.radians(value) if unit == "degrees" else value)
        }
    )

# Route 7: Trigonometry - Tan (app_v1_math)
@app_v1_math.get("/trigonometry/tan")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_trigonometry_tan(
        request: Request,
        background_tasks: BackgroundTasks,
        value: Union[int, float] = Query(..., description="The value of degrees or radians to convert to tan."),
        unit: Literal["degrees", "radians"] = Query(..., description="The unit of the value provided.")
):
    try:
        return utils.send_response(
            request=request,
            status_code=200,
            success=True,
            message=f"Successfully converted the value from {unit} to tan.",
            background_tasks=background_tasks,
            data={
                "result": math.tan(math.radians(value) if unit == "degrees" else value)
            }
        )
    except ZeroDivisionError:
        return utils.send_response(
            request=request,
            status_code=422,
            success=False,
            message="Math Error: The resulting value is undefined (division by zero).",
            background_tasks=background_tasks
        )

# Route 8: Trigonometry - Cosec (app_v1_math)
@app_v1_math.get("/trigonometry/cosec")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_trigonometry_cosec(
        request: Request,
        background_tasks: BackgroundTasks,
        value: Union[int, float] = Query(..., description="The value of degrees or radians to convert to cosec."),
        unit: Literal["degrees", "radians"] = Query(..., description="The unit of the value provided.")
):
    try:
        return utils.send_response(
            request=request,
            status_code=200,
            success=True,
            message=f"Successfully converted the value from {unit} to cosec.",
            background_tasks=background_tasks,
            data={
                "result": 1/math.sin(math.radians(value) if unit == "degrees" else value)
            }
        )
    except ZeroDivisionError:
        return utils.send_response(
            request=request,
            status_code=422,
            success=False,
            message="Math Error: The resulting value is undefined (division by zero).",
            background_tasks=background_tasks
        )

# Route 9: Trigonometry - Sec (app_v1_math)
@app_v1_math.get("/trigonometry/sec")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_trigonometry_sec(
        request: Request,
        background_tasks: BackgroundTasks,
        value: Union[int, float] = Query(..., description="The value of degrees or radians to convert to sec."),
        unit: Literal["degrees", "radians"] = Query(..., description="The unit of the value provided.")
):
    try:
        return utils.send_response(
            request=request,
            status_code=200,
            success=True,
            message=f"Successfully converted the value from {unit} to sec.",
            background_tasks=background_tasks,
            data={
                "result": 1/math.cos(math.radians(value) if unit == "degrees" else value)
            }
        )
    except ZeroDivisionError:
        return utils.send_response(
            request=request,
            status_code=422,
            success=False,
            message="Math Error: The resulting value is undefined (division by zero).",
            background_tasks=background_tasks
        )

# Route 10: Trigonometry - Cot (app_v1_math)
@app_v1_math.get("/trigonometry/cot")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_trigonometry_cot(
        request: Request,
        background_tasks: BackgroundTasks,
        value: Union[int, float] = Query(..., description="The value of degrees or radians to convert to cot."),
        unit: Literal["degrees", "radians"] = Query(..., description="The unit of the value provided.")
):
    try:
        return utils.send_response(
            request=request,
            status_code=200,
            success=True,
            message=f"Successfully converted the value from {unit} to cot.",
            background_tasks=background_tasks,
            data={
                "result": 1/math.tan(math.radians(value) if unit == "degrees" else value)
            }
        )
    except ZeroDivisionError:
        return utils.send_response(
            request=request,
            status_code=422,
            success=False,
            message="Math Error: The resulting value is undefined (division by zero).",
            background_tasks=background_tasks
        )

# Route 11: Statistics (app_v1_math)
@app_v1_math.get("/statistics")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_statistics(request: Request, background_tasks: BackgroundTasks):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Welcome to the 'statistics' sub-utility namespace under 'math'. Check the documentation for available endpoints.",
        background_tasks=background_tasks,
        meta={
            "help": "Check the API v1 documentation (/math) for available endpoints.",
            "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs/v1/3_math.md"
        }
    )

# Route 12: Statistics - Mean (app_v1_math)
@app_v1_math.post("/statistics/mean")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_statistics_mean(
        request: Request,
        background_tasks: BackgroundTasks,
        data: List[Union[int, float]] = Body(..., embed=True, min_length=1, description="The list of values used to calculate the mean.")
):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Successfully calculated the mean of the data.",
        background_tasks=background_tasks,
        data={
            "mean": statistics.mean(data)
        }
    )

# Route 13: Statistics - Median (app_v1_math)
@app_v1_math.post("/statistics/median")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_statistics_median(
        request: Request,
        background_tasks: BackgroundTasks,
        data: List[Union[int, float]] = Body(..., embed=True, min_length=1, description="The list of values used to calculate the median.")
):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Successfully calculated the median of the data.",
        background_tasks=background_tasks,
        data={
            "median": statistics.median(data)
        }
    )

# Route 14: Statistics - Mode (app_v1_math)
@app_v1_math.post("/statistics/mode")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_statistics_mode(
        request: Request,
        background_tasks: BackgroundTasks,
        data: List[Union[int, float]] = Body(..., embed=True, min_length=1, description="The list of values used to calculate the mode.")
):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Successfully calculated the mode of the data.",
        background_tasks=background_tasks,
        data={
            "mode": statistics.multimode(data)
        }
    )