from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uuid

app = FastAPI(
    title="AI Video Creator API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class VideoRequest(BaseModel):
    prompt: str
    duration: str
    language: str
    style: str


@app.get("/")
def home():
    return {
        "message": "AI Video Creator API is running"
    }


@app.post("/create-video")
def create_video(request: VideoRequest):

    job_id = str(uuid.uuid4())

    return {
        "job_id": job_id,
        "status": "queued",
        "message": "Video generation job created",
        "prompt": request.prompt,
        "duration": request.duration,
        "language": request.language,
        "style": request.style
    }
@app.post("/generate-script")
def generate_script(request: VideoRequest):
    script = f"""
Title: {request.prompt}

Language: {request.language}
Style: {request.style}
Duration: {request.duration}

Scene 1:
Introduction about {request.prompt}.

Scene 2:
Explain the main idea clearly.

Scene 3:
Show the important details.

Scene 4:
Give a useful conclusion.
"""

    return {
        "status": "success",
        "script": script
    }
