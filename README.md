# AI--First--CRM--HCP
# AI-First CRM for HCPs - Backend

## Overview
This is the backend of the AI-First CRM for Healthcare Professionals (HCPs). It is built using FastAPI and provides REST APIs for managing HCPs and their interactions.

## Features
- Create and retrieve HCP records
- Create and retrieve interaction records
- AI-powered interaction summary using Groq API
- SQLite database integration
- Interactive Swagger API documentation

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Groq API
- Pydantic

## Project Structure

```text
app/
├── database/
├── models/
├── routes/
├── schemas/
├── services/
└── main.py
```

## Installation

```bash
pip install -r requirements.txt
```

## Run the Server

```bash
python -m uvicorn app.main:app --reload
```

## API Documentation

Open in your browser:

```
http://127.0.0.1:8000/docs
```

## Environment Variable

Create a `.env` file in the backend directory:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

> Do not commit the `.env` file to GitHub.
