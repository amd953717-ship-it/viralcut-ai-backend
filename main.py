from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl, Field
import os, uuid

app = FastAPI(title="ViralCut AI Backend", version="0.1.0")
origin = os.getenv("FRONTEND_ORIGIN", "*")
app.add_middleware(CORSMiddleware, allow_origins=[origin] if origin != "*" else ["*"],
                   allow_credentials=origin != "*", allow_methods=["*"], allow_headers=["*"])

class CreateShortsRequest(BaseModel):
    url: HttpUrl
    quantity: int = Field(ge=2, le=30)
    language: str = "Auto detect"
    style: str = "Viral & dynamic"

@app.get("/")
def root():
    return {"service": "ViralCut AI Backend", "status": "running"}

@app.get("/health")
def health():
    return {"ok": True, "service": "viralcut-ai-backend"}

@app.post("/api/create-shorts", status_code=202)
def create_shorts(request: CreateShortsRequest):
    if request.url.host.lower() not in {"youtube.com", "www.youtube.com", "m.youtube.com", "youtu.be"}:
        return {"error": "Please provide a valid YouTube URL."}
    return {
        "jobId": str(uuid.uuid4()),
        "status": "backend_connected_processing_not_configured",
        "requestedShorts": request.quantity,
        "message": "Backend connected. Actual video processing is not configured yet. Connect an authorized media-ingestion, transcription, AI selection, FFmpeg rendering and storage workflow before generating downloadable clips."
    }
