# Changelog

This is the changelog file of `api.anikethchavare.com`. All notable changes to
this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.5.0] - 2026-04-04

### Added
- Implemented request logging for API requests using Neon (Vercel).
- New `/health` endpoint for performing health checks.
- Implemented universal exception handling with detailed error logging.

### Changed
- Updated `requirements.txt` to include `python-dotenv` and `psycogp2-binary`.

## [0.4.0] - 2026-04-04

### Added
- Implemented global middleware to inject security headers into every API response.
- Added a dedicated exception handler for `404 Not Found` errors.
- Integrated static file handling for `favicon.ico` to improve browser branding and eliminate 404 noise in server logs.
- Created `CREDITS.md` to acknowledge open-source libraries and external service providers.

### Changed
- Moved `utils.py` and `schemas.py` (models) into the `/app` directory for a better structure.
- Renamed the rate limiting exception handler for better code readability.

### Removed
- Removed `response_time_ms` from the `APIResponse` model.
- Updated `.gitignore` to ensure `venv/` is excluded from version control.

## [0.3.0] - 2026-04-03

### Added
- Integrated `SlowAPI` to enforce a 60 RPM limit across all endpoints.
- Added `CORSMiddleware` to allow public cross-origin requests.
- Added a permanent `rate_limit` key to the `meta` object in the `send_response` helper.

### Changed
- Overrode the default `RateLimitExceeded` response to strictly follow the `APIResponse` JSON model instead of plain text.
- Updated `requirements.txt` to include `slowapi`.

### Security
- Implemented **HTTP 429** status codes with structured JSON payloads for rate-limit enforcement.

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
[0.5.0]: https://github.com/anikethchavare/api.anikethchavare.com/releases/tag/v0.5.0
[0.4.0]: https://github.com/anikethchavare/api.anikethchavare.com/releases/tag/v0.4.0
[0.3.0]: https://github.com/anikethchavare/api.anikethchavare.com/releases/tag/v0.3.0
[0.2.0]: https://github.com/anikethchavare/api.anikethchavare.com/releases/tag/v0.2.0
[0.1.0]: https://github.com/anikethchavare/api.anikethchavare.com/releases/tag/v0.1.0