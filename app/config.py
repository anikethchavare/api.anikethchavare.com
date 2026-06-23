# api.anikethchavare.com - app/config.py

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
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Class 1: Settings
class Settings(BaseSettings):
    upstash_redis_url: str = Field(..., alias="UPSTASH_REDIS_URL")
    cron_secret: str = Field(..., alias="CRON_SECRET")
    database_url: str = Field(..., alias="DATABASE_URL")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

# Instantiate "settings" Globally
settings = Settings()