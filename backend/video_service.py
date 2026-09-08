import uuid


def create_video_job(prompt, duration, language, style):
    job_id = str(uuid.uuid4())

    return {
        "job_id": job_id,
        "status": "queued",
        "prompt": prompt,
        "duration": duration,
        "language": language,
        "style": style,
        "message": "Video generation job created successfully"
    }
