import pytest
from unittest.mock import patch, MagicMock
from src.openai_service import (generate_text, translate_text, summarize_text, exponential_backoff)
from src.utils import sanitize_input, format_response, get_model_from_request
from httpx import HTTPStatusError
import openai
import os
import time

@patch('src.openai_service.openai.Completion.create')
def test_generate_text_success(mock_openai_create):
    mock_response = MagicMock()
    mock_response.choices = [{'text': 'This is a test response.'}]
    mock_openai_create.return_value = mock_response
    result = generate_text("Test prompt")
    assert result == "This is a test response."

@patch('src.openai_service.openai.Completion.create')
def test_generate_text_api_error(mock_openai_create):
    mock_openai_create.side_effect = openai.error.OpenAIError("API error")
    with pytest.raises(HTTPException) as excinfo:
        generate_text("Test prompt")
    assert excinfo.value.status_code == 500
    assert "OpenAI API Error" in str(excinfo.value)

@patch('src.openai_service.openai.Completion.create')
def test_generate_text_invalid_prompt(mock_openai_create):
    with pytest.raises(ValueError) as excinfo:
        generate_text("")
    assert "Prompt cannot be empty" in str(excinfo.value)

@patch('src.openai_service.openai.Completion.create')
def test_generate_text_long_prompt(mock_openai_create):
    long_prompt = "a" * 1001
    with pytest.raises(ValueError) as excinfo:
        generate_text(long_prompt)
    assert "exceeds maximum length" in str(excinfo.value)

@patch('src.openai_service.openai.Completion.create')
def test_generate_text_network_error(mock_openai_create):
    mock_openai_create.side_effect = HTTPStatusError('Network error', request=None)
    with pytest.raises(HTTPException) as excinfo:
        generate_text("Test prompt")
    assert excinfo.value.status_code == 500
    assert "Internal Server Error" in str(excinfo.value)


@patch('src.openai_service.openai.Completion.create')
def test_translate_text_success(mock_openai_create):
    mock_response = MagicMock()
    mock_response.choices = [{'text': 'This is a test translation.'}]
    mock_openai_create.return_value = mock_response
    result = translate_text("Test prompt")
    assert result == "This is a test translation."

@patch('src.openai_service.openai.Completion.create')
def test_translate_text_api_error(mock_openai_create):
    mock_openai_create.side_effect = openai.error.OpenAIError("API error")
    with pytest.raises(HTTPException) as excinfo:
        translate_text("Test prompt")
    assert excinfo.value.status_code == 500
    assert "OpenAI API Error" in str(excinfo.value)

@patch('src.openai_service.openai.Completion.create')
def test_summarize_text_success(mock_openai_create):
    mock_response = MagicMock()
    mock_response.choices = [{'text': 'This is a test summary.'}]
    mock_openai_create.return_value = mock_response
    result = summarize_text("Test prompt")
    assert result == "This is a test summary."

@patch('src.openai_service.openai.Completion.create')
def test_summarize_text_api_error(mock_openai_create):
    mock_openai_create.side_effect = openai.error.OpenAIError("API error")
    with pytest.raises(HTTPException) as excinfo:
        summarize_text("Test prompt")
    assert excinfo.value.status_code == 500
    assert "OpenAI API Error" in str(excinfo.value)

@patch('src.openai_service.time.sleep')
def test_exponential_backoff_success(mock_sleep):
    exponential_backoff()
    assert mock_sleep.call_count > 0

@patch('src.openai_service.time.sleep')
def test_exponential_backoff_max_retries(mock_sleep):
    exponential_backoff(max_retries=2)
    assert mock_sleep.call_count == 2

@patch('src.openai_service.openai.Completion.create')
def test_generate_text_invalid_model(mock_openai_create):
    mock_openai_create.side_effect = openai.error.InvalidRequestError("Invalid model")
    with pytest.raises(HTTPException) as excinfo:
        generate_text("Test prompt", model="invalid-model")
    assert excinfo.value.status_code == 400
    assert "Invalid model" in str(excinfo.value)

```