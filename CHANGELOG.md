# Changelog

This is the changelog file of `api.anikethchavare.com`. All notable changes to
this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
[0.1.0]: https://github.com/anikethchavare/api.anikethchavare.com/releases/tag/v0.1.0