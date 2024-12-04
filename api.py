import os
from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from src.openai_service import openai_service
from loguru import logger
from typing import Optional

api_router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str
    model: Optional[str] = "text-davinci-003"
    max_tokens: Optional[int] = 150
    temperature: Optional[float] = 0.7

@api_router.post("/generate", status_code=status.HTTP_200_OK)
async def generate_text(request_body: PromptRequest):
    try:
        response = await openai_service.generate_text(request_body.prompt, request_body.model, request_body.max_tokens, request_body.temperature)
        return {"text": response}
    except HTTPException as e:
        logger.exception(f"HTTPException during text generation: {e}")
        raise e
    except Exception as e:
        logger.exception(f"Unexpected error during text generation: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@api_router.post("/translate", status_code=status.HTTP_200_OK)
async def translate_text(request_body: PromptRequest):
    try:
        response = await openai_service.translate_text(request_body.prompt, request_body.model, request_body.max_tokens, request_body.temperature)
        return {"translation": response}
    except HTTPException as e:
        logger.exception(f"HTTPException during text translation: {e}")
        raise e
    except Exception as e:
        logger.exception(f"Unexpected error during text translation: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@api_router.post("/summarize", status_code=status.HTTP_200_OK)
async def summarize_text(request_body: PromptRequest):
    try:
        response = await openai_service.summarize_text(request_body.prompt, request_body.model, request_body.max_tokens, request_body.temperature)
        return {"summary": response}
    except HTTPException as e:
        logger.exception(f"HTTPException during text summarization: {e}")
        raise e
    except Exception as e:
        logger.exception(f"Unexpected error during text summarization: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

```