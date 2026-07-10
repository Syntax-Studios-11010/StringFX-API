from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from app.core import transformers

app = FastAPI(title="StringFX Processor Engine", version="1.0.0")

# Define the request structure using Pydantic
class ProcessRequest(BaseModel):
    text: str
    pipeline: List[str]

class ProcessResponse(BaseModel):
    input_text: str
    output_text: str
    applied_pipeline: List[str]

@app.post("/v1/process", response_model=ProcessResponse)
async def process_text(request: ProcessRequest):
    current_text = request.text
    
    # Execute the requested pipelines sequentially
    for step in request.pipeline:
        step_lower = step.lower()
        
        if step_lower == "mock":
            current_text = transformers.to_mock_text(current_text)
        elif step_lower == "leet":
            current_text = transformers.to_leet_speak(current_text)
        elif step_lower == "slugify":
            current_text = transformers.to_slugify(current_text)
        elif step_lower == "sanitize":
            current_text = transformers.sanitize_text(current_text)
        else:
            raise HTTPException(
                status_code=400, 
                detail=f"Unknown processor step: '{step}'. Valid steps are: mock, leet, slugify, sanitize"
            )
            
    return ProcessResponse(
        input_text=request.text,
        output_text=current_text,
        applied_pipeline=request.pipeline
    )