# ViralCut AI Backend starter

Deployable FastAPI service for connecting the ViralCut AI frontend.

Endpoints:
- GET / — service status
- GET /health — health check
- POST /api/create-shorts — validates a YouTube URL and returns a job ID

IMPORTANT: This starter confirms backend connectivity only. It does not download videos, detect viral moments, render clips, add captions, or provide downloads. Those require an authorized media-ingestion workflow, transcription/AI services, FFmpeg rendering, job storage, and download endpoints. Only process videos you own or have permission to edit, and comply with platform terms and copyright law.

Render setup: create a Web Service from this repository and select Docker runtime. No API keys are required for this starter.
