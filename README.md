<div class="hero-icon" align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</div>

<h1 align="center">
OpenAI-API-Wrapper-MVP
</h1>
<h4 align="center">Simplified Python backend for OpenAI API access</h4>
<h4 align="center">Developed with the software and tools below.</h4>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue" alt="Programming Language">
  <img src="https://img.shields.io/badge/Framework-FastAPI-red" alt="Web Framework">
  <img src="https://img.shields.io/badge/API-OpenAI-blue" alt="API Used">
  <img src="https://img.shields.io/badge/Logging-Loguru-black" alt="Logging Library">
</div>
<div class="badges" align="center">
  <img src="https://img.shields.io/github/last-commit/YOUR_GITHUB_USERNAME/OpenAI-API-Wrapper-MVP?style=flat-square&color=5D6D7E" alt="Last Commit">
  <img src="https://img.shields.io/github/commit-activity/m/YOUR_GITHUB_USERNAME/OpenAI-API-Wrapper-MVP?style=flat-square&color=5D6D7E" alt="Commit Activity">
  <img src="https://img.shields.io/github/languages/top/YOUR_GITHUB_USERNAME/OpenAI-API-Wrapper-MVP?style=flat-square&color=5D6D7E" alt="Top Language">
</div>

## 📑 Table of Contents
- 📍 Overview
- 📦 Features
- 📂 Structure
- 💻 Installation
- 🏗️ Usage
- 🌐 Hosting
- 📄 License
- 👏 Authors

## 📍 Overview
This repository contains a Minimum Viable Product (MVP) that simplifies access to OpenAI's API.  It provides a Python-based RESTful API built with FastAPI, handling requests, interacting with the OpenAI API, and returning processed responses. The MVP focuses on ease of use and reliability, abstracting away the complexities of direct API interaction.

## 📦 Features
|    | Feature                      | Description                                                                                                                                   |
|----|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | Request Handling & Validation | Accepts user prompts, validates input length and format, and prepares data for the OpenAI API.                                                        |
| 2  | OpenAI API Interaction        | Sends requests to the OpenAI API, handles API key authentication, manages rate limits using exponential backoff, and handles API errors gracefully. |
| 3  | Response Processing           | Receives and parses JSON responses, extracts generated text, and formats it for user consumption. Handles potential parsing errors.                     |
| 4  | Comprehensive Error Handling  | Provides informative error messages to the user and detailed logging for debugging. Distinguishes between client-side and server-side errors.         |


## 📂 Structure
```text
openai-wrapper-mvp/
├── src/
│   ├── main.py
│   ├── api/
│   │   └── routes.py
│   ├── openai_service.py
│   ├── utils.py
│   └── __init__.py
├── .env
├── requirements.txt
├── Dockerfile
└── tests/
    └── test_api.py
    └── test_services.py

```

## 💻 Installation
### 🔧 Prerequisites
- Python 3.9+
- `pip`

### 🚀 Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/OpenAI-API-Wrapper-MVP.git
   cd OpenAI-API-Wrapper-MVP
   ```
2. Create a `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🏗️ Usage
### 🏃‍♂️ Running the MVP
```bash
python src/main.py
```
The API will be available at `http://localhost:8000`.

### ⚙️ Configuration
The API key is loaded from the `.env` file.  The port can be changed by setting the `PORT` environment variable.

### 📚 Examples
- **Text Generation:**  `POST /generate` with a JSON body like `{"prompt": "Write a short story"}`

## 🌐 Hosting
Deploy using Docker:
1. Build the Docker image: `docker build -t openai-api-wrapper .`
2. Run the container: `docker run -p 8000:8000 openai-api-wrapper`


## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👏 Authors
- YOUR_NAME


<p align="center">
  <h1 align="center">🌐 CosLynx.com</h1>
</p>
<p align="center">
  <em>Create Your Custom MVP in Minutes With CosLynxAI!</em>
</p>
<div class="badges" align="center">
<img src="https://img.shields.io/badge/Developers-Drix10,_Kais_Radwan-red" alt="">
<img src="https://img.shields.io/badge/Website-CosLynx.com-blue" alt="">
<img src="https://img.shields.io/badge/Backed_by-Google,_Microsoft_&_Amazon_for_Startups-red" alt="">
<img src="https://img.shields.io/badge/Finalist-Backdrop_Build_v4,_v6-black" alt="">
</div>
```