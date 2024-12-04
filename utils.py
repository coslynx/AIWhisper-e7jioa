import re
from typing import Optional

def validate_prompt(prompt: str, max_length: int = 1000) -> str:
    """Validates the user prompt.

    Args:
        prompt: The user's prompt.
        max_length: The maximum allowed length of the prompt.

    Returns:
        The validated prompt if it's valid; otherwise, raises a ValueError.
    """
    prompt = prompt.strip()
    if not prompt:
        raise ValueError("Prompt cannot be empty.")
    if len(prompt) > max_length:
        raise ValueError(f"Prompt exceeds maximum length of {max_length} characters.")
    return prompt

def format_response(response: dict) -> str:
    """Formats the response from the OpenAI API.

    Args:
        response: The raw JSON response from the OpenAI API.

    Returns:
        The formatted response text.  Raises a ValueError if the response is invalid.
    """
    try:
        text = response['choices'][0]['text'].strip()
        return text
    except (KeyError, IndexError):
        raise ValueError("Invalid response format from OpenAI API.")

def extract_translation(response: dict) -> str:
    """Extracts translation from the response.

    Args:
      response: Dictionary containing the OpenAI API response.

    Returns:
      The translated text. Raises ValueError if translation is not found.
    """
    try:
        return response['choices'][0]['text'].strip()
    except (KeyError, IndexError):
        raise ValueError("Translation not found in response.")

def extract_summary(response: dict) -> str:
    """Extracts summary from the response.

    Args:
      response: Dictionary containing the OpenAI API response.

    Returns:
      The summarized text. Raises ValueError if summary is not found.
    """
    try:
        return response['choices'][0]['text'].strip()
    except (KeyError, IndexError):
        raise ValueError("Summary not found in response.")


def sanitize_input(text: str) -> str:
    """Sanitizes user input to prevent injection attacks."""
    # Basic sanitization - replace potentially harmful characters
    sanitized_text = re.sub(r"[<>\"]", "", text) 
    return sanitized_text

def get_model_from_request(model: Optional[str] = "text-davinci-003") -> str:
    """Retrieves the OpenAI model from the request, defaulting to text-davinci-003"""
    return model or "text-davinci-003"

```