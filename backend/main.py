from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from video_service import create_video_job


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
    job = create_video_job(
        request.prompt,
        request.duration,
        request.language,
        request.style
    )

    return job
