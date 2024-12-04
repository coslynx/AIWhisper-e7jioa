import os
import openai
from loguru import logger
from typing import Optional
from src.utils import sanitize_input, format_response, get_model_from_request
import time
import random

logger.add("openai_service.log", rotation="10 MB", level="DEBUG")

openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_text(prompt: str, model: Optional[str] = "text-davinci-003", max_tokens: Optional[int] = 150, temperature: Optional[float] = 0.7) -> str:
    sanitized_prompt = sanitize_input(prompt)
    model = get_model_from_request(model)
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=sanitized_prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=temperature,
        )
        return format_response(response)
    except openai.error.OpenAIError as e:
        logger.exception(f"OpenAI API error during text generation: {e}, Prompt: {sanitized_prompt}")
        raise HTTPException(status_code=500, detail=f"OpenAI API Error: {e}")
    except Exception as e:
        logger.exception(f"Unexpected error during text generation: {e}, Prompt: {sanitized_prompt}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

async def translate_text(prompt: str, model: Optional[str] = "text-davinci-003", max_tokens: Optional[int] = 150, temperature: Optional[float] = 0.7) -> str:
    sanitized_prompt = sanitize_input(prompt)
    model = get_model_from_request(model)
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=sanitized_prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=temperature,
        )
        return format_response(response)
    except openai.error.OpenAIError as e:
        logger.exception(f"OpenAI API error during text translation: {e}, Prompt: {sanitized_prompt}")
        raise HTTPException(status_code=500, detail=f"OpenAI API Error: {e}")
    except Exception as e:
        logger.exception(f"Unexpected error during text translation: {e}, Prompt: {sanitized_prompt}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

async def summarize_text(prompt: str, model: Optional[str] = "text-davinci-003", max_tokens: Optional[int] = 150, temperature: Optional[float] = 0.7) -> str:
    sanitized_prompt = sanitize_input(prompt)
    model = get_model_from_request(model)
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=sanitized_prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=temperature,
        )
        return format_response(response)
    except openai.error.OpenAIError as e:
        logger.exception(f"OpenAI API error during text summarization: {e}, Prompt: {sanitized_prompt}")
        raise HTTPException(status_code=500, detail=f"OpenAI API Error: {e}")
    except Exception as e:
        logger.exception(f"Unexpected error during text summarization: {e}, Prompt: {sanitized_prompt}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

def exponential_backoff(max_retries: int = 5, initial_delay: int = 1) -> None:
    for i in range(max_retries):
        delay = initial_delay * (2**i) + random.uniform(0, 1)  # Add some jitter
        time.sleep(delay)

```