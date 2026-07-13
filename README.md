# AutoPilot – Scheduled AI Agent

## Overview

AutoPilot is an AI-powered backend service that runs scheduled jobs using APScheduler and a local Ollama model.

## Technologies

- Python
- APScheduler
- Ollama
- SQLAlchemy
- SQLite
- FastAPI (Coming in Week 2)

## Project Structure

```
AutoPilot/
│
├── app/
├── scheduler/
├── llm/
├── database/
├── logs/
├── tests/
├── config/
├── utils/
├── main.py
```

## Current Features

- Scheduler starts automatically.
- Jobs run every minute.
- Ollama is called locally.
- AI responses are logged.
- Jobs persist after restart.

## Run

```bash
python main.py
```