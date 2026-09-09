import uuid

jobs = {}


def create_video_job(prompt, duration, language, style):
    job_id = str(uuid.uuid4())

    jobs[job_id] = {
        "job_id": job_id,
        "status": "queued",
        "prompt": prompt,
        "duration": duration,
        "language": language,
        "style": style
    }

    return jobs[job_id]


def get_video_job(job_id):
    return jobs.get(job_id)
