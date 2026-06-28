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
import cmath
import statistics
import numpy as np
from pydantic import StrictInt, StrictFloat
from typing import Union, Literal, List

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
            message="MathError: The resulting value is undefined (division by zero).",
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
            message="MathError: The resulting value is undefined (division by zero).",
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
        data: List[Union[StrictInt, StrictFloat]] = Body(..., embed=True, min_length=1, description="The list of values used to calculate the mean.")
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
        data: List[Union[StrictInt, StrictFloat]] = Body(..., embed=True, min_length=1, description="The list of values used to calculate the median.")
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
        data: List[Union[StrictInt, StrictFloat]] = Body(..., embed=True, min_length=1, description="The list of values used to calculate the mode.")
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

# Route 15: Algebra (app_v1_math)
@app_v1_math.get("/algebra")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_algebra(request: Request, background_tasks: BackgroundTasks):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Welcome to the 'algebra' sub-utility namespace under 'math'. Check the documentation for available endpoints.",
        background_tasks=background_tasks,
        meta={
            "help": "Check the API v1 documentation (/math) for available endpoints.",
            "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs/v1/3_math.md"
        }
    )

# Route 16: Algebra - Discriminant (app_v1_math)
@app_v1_math.post("/algebra/discriminant")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_algebra_discriminant(
        request: Request,
        background_tasks: BackgroundTasks,
        coefficients: List[Union[StrictInt, StrictFloat]] = Body(..., embed=True, min_length=3, max_length=4, description="The list of coefficients of an equation.")
):
    if coefficients[0] == 0:
        return utils.send_response(
            request=request,
            status_code=422,
            success=False,
            message="MathError: The first coefficient (a) of an equation must not be zero.",
            background_tasks=background_tasks
        )

    if len(coefficients) == 3:
        a, b, c = coefficients
        discriminant = (b**2) - (4*a*c)
    else:
        a, b, c, d = coefficients
        discriminant = ((b**2)*(c**2)) - (4*a*(c**3)) - (4*(b**3)*d) - (27*(a**2)*(d**2)) + (18*a*b*c*d)

    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message=f"Successfully calculated the discriminant of the {'quadratic' if len(coefficients) == 3 else 'cubic'} equation.",
        background_tasks=background_tasks,
        data={
            "discriminant": discriminant
        }
    )

# Route 17: Algebra - Roots (app_v1_math)
@app_v1_math.post("/algebra/roots")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_algebra_roots(
        request: Request,
        background_tasks: BackgroundTasks,
        coefficients: List[Union[StrictInt, StrictFloat]] = Body(..., embed=True, min_length=3, max_length=4, description="The list of coefficients of an equation.")
):
    if coefficients[0] == 0:
        return utils.send_response(
            request=request,
            status_code=422,
            success=False,
            message="MathError: The first coefficient (a) of an equation must not be zero.",
            background_tasks=background_tasks
        )

    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message=f"Successfully calculated the roots of the {'quadratic' if len(coefficients) == 3 else 'cubic'} equation.",
        background_tasks=background_tasks,
        data={
            "roots": [r.item().real if np.isreal(r) else str(r.item()) for r in np.roots(coefficients)]
        }
    )

# Route 18: Arithmetic (app_v1_math)
@app_v1_math.get("/arithmetic")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_arithmetic(request: Request, background_tasks: BackgroundTasks):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Welcome to the 'arithmetic' sub-utility namespace under 'math'. Check the documentation for available endpoints.",
        background_tasks=background_tasks,
        meta={
            "help": "Check the API v1 documentation (/math) for available endpoints.",
            "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs/v1/3_math.md"
        }
    )

# Route 19: Arithmetic - Factorial (app_v1_math)
@app_v1_math.get("/arithmetic/factorial")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_arithmetic_factorial(
        request: Request,
        background_tasks: BackgroundTasks,
        n: int = Query(..., ge=0, description="The non-negative integer used to compute the factorial.")
):
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i

    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Successfully calculated the factorial.",
        background_tasks=background_tasks,
        data={
            "factorial": factorial
        }
    )

# Route 20: Arithmetic - Is Prime (app_v1_math)
@app_v1_math.get("/arithmetic/is-prime")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_arithmetic_is_prime(
        request: Request,
        background_tasks: BackgroundTasks,
        n: int = Query(..., ge=2, description="The target integer to evaluate for primality (must be greater than or equal to 2).")
):
    is_prime = True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False

    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Successfully tested the number for primality.",
        background_tasks=background_tasks,
        data={
            "is_prime": is_prime
        }
    )

# Route 21: Arithmetic - Is Even (app_v1_math)
@app_v1_math.get("/arithmetic/is-even")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_arithmetic_is_even(
        request: Request,
        background_tasks: BackgroundTasks,
        n: int = Query(..., description="The target integer to evaluate for even parity.")
):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Successfully tested the number for even parity.",
        background_tasks=background_tasks,
        data={
            "is_even": n % 2 == 0
        }
    )

# Route 22: Arithmetic - Is Odd (app_v1_math)
@app_v1_math.get("/arithmetic/is-odd")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_arithmetic_is_odd(
        request: Request,
        background_tasks: BackgroundTasks,
        n: int = Query(..., description="The target integer to evaluate for odd parity.")
):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Successfully tested the number for odd parity.",
        background_tasks=background_tasks,
        data={
            "is_odd": n % 2 == 1
        }
    )

# Route 23: Arithmetic - HCF (app_v1_math)
@app_v1_math.post("/arithmetic/hcf")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_arithmetic_hcf(
        request: Request,
        background_tasks: BackgroundTasks,
        data: List[StrictInt] = Body(..., embed=True, min_length=1, description="The list of values used to calculate the HCF.")
):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Successfully calculated the HCF of the given values.",
        background_tasks=background_tasks,
        data={
            "hcf": math.gcd(*data)
        }
    )

# Route 24: Arithmetic - LCM (app_v1_math)
@app_v1_math.post("/arithmetic/lcm")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_arithmetic_lcm(
        request: Request,
        background_tasks: BackgroundTasks,
        data: List[StrictInt] = Body(..., embed=True, min_length=1, description="The list of values used to calculate the LCM.")
):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Successfully calculated the LCM of the given values.",
        background_tasks=background_tasks,
        data={
            "lcm": math.lcm(*data)
        }
    )

# Route 25: Arithmetic - Fibonacci (app_v1_math)
@app_v1_math.get("/arithmetic/fibonacci")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_arithmetic_fibonacci(
        request: Request,
        background_tasks: BackgroundTasks,
        n: int = Query(..., ge=1, description="The number of terms to generate in the Fibonacci sequence.")
):
    if n == 1:
        fibonacci_list = [0]
    elif n == 2:
        fibonacci_list = [0, 1]
    else:
        fibonacci_list = [0, 1]

        while len(fibonacci_list) < n:
            fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Successfully generated the Fibonacci sequence.",
        background_tasks=background_tasks,
        data={
            "fibonacci_series": fibonacci_list
        }
    )

# Route 26: Complex (app_v1_math)
@app_v1_math.get("/complex")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_complex(request: Request, background_tasks: BackgroundTasks):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Welcome to the 'complex' sub-utility namespace under 'math'. Check the documentation for available endpoints.",
        background_tasks=background_tasks,
        meta={
            "help": "Check the API v1 documentation (/math) for available endpoints.",
            "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs/v1/3_math.md"
        }
    )

# Route 27: Complex - Modulus (app_v1_math)
@app_v1_math.get("/complex/modulus")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_complex_modulus(
        request: Request,
        background_tasks: BackgroundTasks,
        real: float = Query(..., description="The real component of the complex number"),
        imaginary: float = Query(..., description="The imaginary component of the complex number")
):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Successfully calculated the modulus of the complex number.",
        background_tasks=background_tasks,
        data={
            "modulus": abs(complex(real, imaginary))
        }
    )

# Route 28: Complex - Conjugate (app_v1_math)
@app_v1_math.get("/complex/conjugate")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_complex_conjugate(
        request: Request,
        background_tasks: BackgroundTasks,
        real: float = Query(..., description="The real component of the complex number"),
        imaginary: float = Query(..., description="The imaginary component of the complex number")
):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Successfully calculated the conjugate of the complex number.",
        background_tasks=background_tasks,
        data={
            "conjugate": str(complex(real, imaginary).conjugate())
        }
    )

# Route 29: Complex - Multiplicative Inverse (app_v1_math)
@app_v1_math.get("/complex/multiplicative-inverse")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_complex_multiplicative_inverse(
        request: Request,
        background_tasks: BackgroundTasks,
        real: float = Query(..., description="The real component of the complex number"),
        imaginary: float = Query(..., description="The imaginary component of the complex number")
):
    if real == 0 and imaginary == 0:
        return utils.send_response(
            request=request,
            status_code=422,
            success=False,
            message="MathError: Multiplicative inverse of zero is undefined.",
            background_tasks=background_tasks
        )

    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Successfully calculated the multiplicative inverse of the complex number.",
        background_tasks=background_tasks,
        data={
            "multiplicative_inverse": str(complex(real, imaginary).conjugate()/(abs(complex(real, imaginary))**2))
        }
    )

# Route 30: Complex - Polar (app_v1_math)
@app_v1_math.get("/complex/polar")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_complex_polar(
        request: Request,
        background_tasks: BackgroundTasks,
        real: float = Query(..., description="The real component of the complex number"),
        imaginary: float = Query(..., description="The imaginary component of the complex number")
):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Successfully converted the complex number to polar form.",
        background_tasks=background_tasks,
        data={
            "polar_coordinates": list(cmath.polar(complex(real, imaginary)))
        }
    )

# Route 31: Geometry (app_v1_math)
@app_v1_math.get("/geometry")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_geometry(request: Request, background_tasks: BackgroundTasks):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Welcome to the 'geometry' sub-utility namespace under 'math'. Check the documentation for available endpoints.",
        background_tasks=background_tasks,
        meta={
            "help": "Check the API v1 documentation (/math) for available endpoints.",
            "docs": "https://github.com/anikethchavare/api.anikethchavare.com/tree/main/docs/v1/3_math.md"
        }
    )

# Route 32: Geometry - Circumference (app_v1_math)
@app_v1_math.get("/geometry/circumference")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_geometry_circumference(
        request: Request,
        background_tasks: BackgroundTasks,
        radius: Union[int, float] = Query(..., ge=0, description="The radius of the circle.")
):
    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Successfully calculated the circumference of the circle.",
        background_tasks=background_tasks,
        data={
            "circumference": 2*math.pi*radius
        }
    )

# Route 33: Geometry - Area of Sector (app_v1_math)
@app_v1_math.get("/geometry/area-of-sector")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_geometry_area_of_sector(
        request: Request,
        background_tasks: BackgroundTasks,
        radius: Union[int, float] = Query(..., ge=0, description="The radius of the circle."),
        angle: Union[int, float] = Query(..., ge=0, description="The central angle of the circle."),
        unit: Literal["degrees", "radians"] = Query(..., description="The unit of the value provided.")
):
    if unit == "degrees" and angle > 360:
        return utils.send_response(
            request=request,
            status_code=422,
            success=False,
            message="Validation Error (Math): Angle in degrees cannot exceed 360. ",
            background_tasks=background_tasks
        )

    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Successfully calculated the area of the sector of the circle.",
        background_tasks=background_tasks,
        data={
            "area_of_sector": (angle/360) * math.pi*(radius**2) if unit == "degrees" else 0.5*(radius**2)*angle,
        }
    )

# Route 34: Geometry - Arc Length (app_v1_math)
@app_v1_math.get("/geometry/arc-length")
@rate_limiter.limiter.limit("60/minute")
async def app_v1_math_geometry_arc_length(
        request: Request,
        background_tasks: BackgroundTasks,
        radius: Union[int, float] = Query(..., ge=0, description="The radius of the circle."),
        angle: Union[int, float] = Query(..., ge=0, description="The central angle of the circle."),
        unit: Literal["degrees", "radians"] = Query(..., description="The unit of the value provided.")
):
    if unit == "degrees" and angle > 360:
        return utils.send_response(
            request=request,
            status_code=422,
            success=False,
            message="Validation Error (Math): Angle in degrees cannot exceed 360. ",
            background_tasks=background_tasks
        )

    return utils.send_response(
        request=request,
        status_code=200,
        success=True,
        message="Successfully calculated the arc length of the circle.",
        background_tasks=background_tasks,
        data={
            "arc_length": 2*math.pi*radius*(angle/360) if unit == "degrees" else radius*angle,
        }
    )