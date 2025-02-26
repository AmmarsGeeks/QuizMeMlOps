# QuizMLOps: Automated Quiz Pipeline with MLOps

# MY App on App Store Called Quiz Me
## in this task i have used the (staging data) on the app to complete the task instead of relying on separate api's 

### the app url
https://apps.apple.com/sa/app/quizme-%D8%A7%D8%AE%D8%AA%D8%A8%D8%B1%D9%86%D9%8A/id6739629798

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.103-green)](https://fastapi.tiangolo.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-1.12-red)](https://openai.com/)

## Overview
This project automates quiz processing using MLOps practices. It fetches quiz data from a Firebase API, cleans it, integrates with OpenAI for question answering, and deploys the pipeline via FastAPI. Designed for educational use cases.

## Features
- **Data Extraction**: Fetch quiz data from Firebase Firestore
- **Text Cleaning**: Format questions/answers for LLM compatibility
- **LLM Integration**: OpenAI GPT-3.5/4 for answer generation
- **API Deployment**: FastAPI endpoints for pipeline interaction
- **MLOps Practices**: Modular code

## Installation

### Prerequisites
- Python 3.9+
- Firebase credentials (`service-account-file.json`)
- OpenAI API key

### Setup
```bash
# Clone repository
git clone https://github.com/your-username/QuizMLOps.git
cd QuizMLOps

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Add your OpenAI API key to .env
Usage
Run the application by executing:

python main.py

Project Structure
📦QuizMLOps
┣ 📂app
┃ ┣ 📂api
┃ ┃ ┗ 📜endpoints.py # FastAPI routes
┃ ┣ 📂models
┃ ┃ ┗ 📜qa_model.py # OpenAI integration
┃ ┣ 📂services
┃ ┃ ┣ 📜data_cleaner.py # Data processing
┃ ┃ ┗ 📜data_fetcher.py # API client
┃ ┗ 📜config.py # Environment config
┣ 📂pipeline
┃ ┗ 📜quiz_pipeline.py # Data processing workflow
┣ 📂tests
┣ 📜requirements.txt # Dependencies
┗ 📜README.md # You are here

API Reference
GET /tests
Fetch processed quiz data:

curl http://localhost:8000/tests

POST /ask
Generate answers using OpenAI:

curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is CMOS?", "context": "CMOS technology reduces power consumption..."}'

Deployment
Local Deployment

uvicorn app.api.endpoints:router --host 0.0.0.0 --port 8000


Acknowledgments
OpenAI API for LLM integration
Firebase for data storage
FastAPI for deployment
