from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import uuid
import asyncio
import datetime

app = FastAPI(title="OSINT Pilot Backend")

# Mock Database for investigations
investigations = {}

class TargetInfo(BaseModel):
    first_name: str
    last_name: str
    city: Optional[str] = None
    state: Optional[str] = None
    dob: Optional[str] = None
    birth_year: Optional[str] = None
    username: Optional[str] = None
    ip_address: Optional[str] = None
    notes: Optional[str] = None

class InvestigationStatus(BaseModel):
    job_id: str
    status: str # queued, searching, reporting, completed
    progress: int
    result_url: Optional[str] = None

async def run_osint_pipeline(job_id: str, target: TargetInfo):
    """
    Simulates the multi-agent OSINT pipeline.
    """
    # Step 1: Queued -> Searching
    investigations[job_id] = {"status": "searching", "progress": 10}
    await asyncio.sleep(5) # Simulate database lookup

    # Step 2: Searching Social Media
    investigations[job_id] = {"status": "searching", "progress": 30}
    await asyncio.sleep(5) # Simulate social scraping

    # Step 3: Searching Public Records
    investigations[job_id] = {"status": "searching", "progress": 60}
    await asyncio.sleep(5) # Simulate public record search

    # Step 4: Generating Intelligence Report
    investigations[job_id] = {"status": "reporting", "progress": 80}
    await asyncio.sleep(5) # Simulate AI synthesis

    # Step 5: Completed
    investigations[job_id] = {
        "status": "completed",
        "progress": 100,
        "result_url": f"/reports/{job_id}.pdf"
    }

@app.post("/investigate")
async def start_investigation(target: TargetInfo, background_tasks: BackgroundTasks):
    job_id = str(uuid.uuid4())
    investigations[job_id] = {"status": "queued", "progress": 0}

    background_tasks.add_task(run_osint_pipeline, job_id, target)

    return {"job_id": job_id, "status": "queued", "message": "Investigation started."}

@app.get("/status/{job_id}")
async def get_status(job_id: str):
    if job_id not in investigations:
        raise HTTPException(status_code=404, detail="Investigation not found")
    return {"job_id": job_id, **investigations[job_id]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
