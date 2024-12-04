import pytest
from fastapi.testclient import TestClient
from src.main import app
from unittest.mock import patch
import os

client = TestClient(app)

# Test cases for /generate endpoint
def test_generate_text_simple_prompt():
    response = client.post("/generate", json={"prompt": "Write a short story"})
    assert response.status_code == 200
    assert "text" in response.json()
    assert len(response.json()["text"]) > 0

def test_generate_text_long_prompt():
    long_prompt = "This is a very long prompt to test the API's ability to handle longer inputs. It should be long enough to exceed the default max_tokens limit, but not so long as to cause a server error." * 10
    response = client.post("/generate", json={"prompt": long_prompt, "max_tokens": 500})
    assert response.status_code == 200
    assert "text" in response.json()
    assert len(response.json()["text"]) > 0

def test_generate_text_invalid_prompt():
    response = client.post("/generate", json={"prompt": ""})
    assert response.status_code == 422

def test_generate_text_exceed_max_length():
    long_prompt = "a"*1001
    response = client.post("/generate", json={"prompt": long_prompt})
    assert response.status_code == 422


# Test cases for /translate endpoint
def test_translate_text_simple_prompt():
    response = client.post("/translate", json={"prompt": "Hello, world!", "model": "text-davinci-003"})
    assert response.status_code == 200
    assert "translation" in response.json()
    assert len(response.json()["translation"]) > 0

def test_translate_text_invalid_prompt():
    response = client.post("/translate", json={"prompt": ""})
    assert response.status_code == 422

# Test cases for /summarize endpoint
def test_summarize_text_simple_prompt():
    response = client.post("/summarize", json={"prompt": "The quick brown fox jumps over the lazy dog."})
    assert response.status_code == 200
    assert "summary" in response.json()
    assert len(response.json()["summary"]) > 0

def test_summarize_text_long_prompt():
    long_prompt = "This is a long text that needs to be summarized. It contains multiple sentences and paragraphs to test the summarization capabilities of the API.  The summary should be concise and capture the main points." * 10
    response = client.post("/summarize", json={"prompt": long_prompt, "max_tokens": 100})
    assert response.status_code == 200
    assert "summary" in response.json()
    assert len(response.json()["summary"]) > 0

def test_summarize_text_invalid_prompt():
    response = client.post("/summarize", json={"prompt": ""})
    assert response.status_code == 422

@patch('src.openai_service.openai.Completion.create')
def test_api_error_handling(mock_openai_create):
    mock_openai_create.side_effect = openai.error.OpenAIError("Test API Error")
    response = client.post("/generate", json={"prompt": "test"})
    assert response.status_code == 500
    assert "OpenAI API Error" in response.json()["detail"]

@patch.dict(os.environ, {"OPENAI_API_KEY": ""})
@patch('src.openai_service.openai.Completion.create')
def test_invalid_api_key(mock_openai_create):
    response = client.post("/generate", json={"prompt": "test"})
    assert response.status_code == 500

@patch('src.openai_service.openai.Completion.create')
def test_network_error(mock_openai_create):
    mock_openai_create.side_effect = Exception("Network Error")
    response = client.post("/generate", json={"prompt": "test"})
    assert response.status_code == 500
    assert "Internal Server Error" in response.json()["detail"]

```