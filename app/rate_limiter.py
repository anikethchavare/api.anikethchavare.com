# api.anikethchavare.com - app/rate_limiter.py

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
from slowapi import Limiter
from dotenv import load_dotenv
from slowapi.util import get_remote_address

# Loading Environment Variables
load_dotenv()

# Initializing the Limiter
limiter = Limiter(key_func=get_remote_address,
                  storage_uri=os.getenv("UPSTASH_REDIS_URL", "memory://"),
                  default_limits=["60/minute"])