def create_video_job(prompt, duration, language, style):
    return {
        "status": "queued",
        "prompt": prompt,
        "duration": duration,
        "language": language,
        "style": style,
        "message": "Video generation service is ready"
    }
