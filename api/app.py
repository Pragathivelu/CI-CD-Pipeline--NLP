from fastapi import FastAPI
from src.pipeline.inference_pipeline import run_pipeline

app = FastAPI()

@app.post("/analyze")
def analyze(data: dict):
    return run_pipeline(data["resume"], data["jd"])