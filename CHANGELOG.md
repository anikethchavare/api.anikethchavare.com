# Changelog

This is the changelog file of `api.anikethchavare.com`. All notable changes to
this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Planned: Rate limiting middleware for public endpoints (60 RPM).

## [0.2.0] - 2026-04-03

### Added
- Implemented a centralized `send_response` helper function for unified JSON output.
- Integrated HTTP middleware to automatically calculate `response_time_ms`.
- Added ISO 8601 UTC timestamps and full UUID-based `request_id` to all responses.
- Expanded `APIResponse` schema to include precision metadata and status codes.

## [0.1.0] - 2026-04-03

### Added
- Initialized FastAPI server entry point in `server.py`.
- Defined a standardized `APIResponse` schema in `schema.py` for predictable
JSON output.
- Implemented strict dictionary defaults (`{}`) for `data` and `meta` fields to
ensure frontend stability.
- Configured deployment settings for Vercel via `vercel.json`.
- Added project metadata including `LICENSE.txt` (Apache 2.0) and `.gitignore`.
- Established `requirements.txt` with core dependencies (FastAPI, Pydantic).

---
[0.2.0]: https://github.com/anikethchavare/api.anikethchavare.com/releases/tag/v0.2.0
[0.1.0]: https://github.com/anikethchavare/api.anikethchavare.com/releases/tag/v0.1.0