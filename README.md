# AutoPilot

> An automated AI-powered email processing system that monitors Gmail, summarizes unread emails using a local Ollama LLM, stores summaries locally, and delivers them to Slack on a configurable schedule.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Gmail Setup](#gmail-setup)
- [Ollama Setup](#ollama-setup)
- [Slack Setup](#slack-setup)
- [Running the Project](#running-the-project)
- [Scheduler Configuration](#scheduler-configuration)
- [Output and Logs](#output-and-logs)
- [Error Handling and Reliability](#error-handling-and-reliability)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [Security](#security)
- [Customisation](#customisation)
- [Future Improvements](#future-improvements)
- [Project Status](#project-status)
- [License](#license)

---

# Overview

AutoPilot is a Python-based automation system designed to process emails without requiring manual summarization.

The system connects to a Gmail inbox using IMAP, identifies unread emails, extracts and cleans their contents, sends them to a locally running Ollama language model for summarization, saves the generated summaries, and sends the results to a configured Slack channel.

The application can be:

- Run manually when required.
- Run automatically using APScheduler.
- Configured to execute at specific times using interval or cron-based scheduling.

The complete workflow is:

```text
                    ┌──────────────────────┐
                    │      Scheduler       │
                    │     APScheduler      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       ai_job()       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Email Pipeline    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Gmail / IMAP      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Unread Email Search  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Parse & Clean Email  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Ollama Local LLM   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Save Summary       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Slack Webhook      │
                    └──────────────────────┘
````

---

# Features

## Email Processing

* Connects to Gmail using IMAP.
* Searches specifically for unread emails.
* Processes multiple unread emails in a single run.
* Extracts sender, subject, and body.
* Cleans email content before summarization.

## AI Summarization

* Uses a locally running Ollama model.
* Model can be changed through configuration.
* Does not require a cloud LLM API.
* Supports models available through Ollama.

## Slack Integration

* Sends generated summaries to Slack.
* Uses Slack Incoming Webhooks.
* Formats summaries before sending.

## Automation

* Supports scheduled execution through APScheduler.
* Supports interval-based scheduling.
* Supports cron-based scheduling.
* Uses SQLite-backed persistent job storage.

## Reliability

* Retry mechanisms for external operations.
* Error handling for Gmail, Ollama, and Slack.
* Structured application logging.
* Handles situations where no unread emails are available.
* Handles Ollama model loading delays.

## Local Storage

Generated summaries are stored locally in the `summaries/` directory.

---

# How It Works

The system consists of several stages.

### 1. Scheduler

APScheduler starts the configured job.

```text
Scheduler
    ↓
ai_job()
```

### 2. Pipeline

The scheduled job calls the main email-processing pipeline.

```text
ai_job()
    ↓
run_pipeline()
```

### 3. Gmail

The pipeline connects to Gmail and searches for unread emails.

```text
Gmail
    ↓
IMAP
    ↓
Unread Emails
```

### 4. Email Processing

Each unread email is fetched, parsed, and cleaned.

```text
Raw Email
    ↓
Parser
    ↓
Clean Email Data
```

### 5. AI Summarization

The cleaned email is passed to the configured Ollama model.

```text
Clean Email
    ↓
Ollama
    ↓
Summary
```

### 6. Storage

The generated summary is saved locally.

```text
Summary
    ↓
summaries/
```

### 7. Slack

The summary is formatted and sent to Slack.

```text
Summary
    ↓
Slack Formatter
    ↓
Slack Webhook
    ↓
Slack Channel
```

---

# Architecture

```text
                         AutoPilot
                            │
             ┌──────────────┴──────────────┐
             │                             │
        Manual Run                    Scheduler
        main.py                    run_scheduler.py
             │                             │
             └──────────────┬──────────────┘
                            │
                            ▼
                       pipeline.py
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
   email_service/    llm_service/      slack_service/
          │                 │                 │
          ▼                 ▼                 ▼
       Gmail              Ollama            Slack
          │                 │                 │
          └─────────────────┼─────────────────┘
                            │
                            ▼
                         Logging
```

---

# Project Structure

```text
AutoPilot/
│
├── config/
│   └── settings.py
│
├── email_service/
│   ├── imap_client.py
│   └── parser.py
│
├── exceptions/
│   └── custom_exceptions.py
│
├── llm_service/
│   ├── summarizer.py
│   └── summary_writer.py
│
├── scheduler/
│   ├── scheduler.py
│   └── jobs.py
│
├── slack_service/
│   ├── formatter.py
│   └── slack_client.py
│
├── utils/
│   └── logger.py
│
├── summaries/
│
├── logs/
│
├── .env
├── .gitignore
├── main.py
├── pipeline.py
├── run_scheduler.py
├── requirements.txt
├── jobs.sqlite
└── README.md
```

> `summaries/`, `logs/`, `.env`, and local database files should generally not be committed to a public repository.

---

# Technology Stack

| Technology     | Purpose                          |
| -------------- | -------------------------------- |
| Python         | Core application                 |
| Gmail IMAP     | Email retrieval                  |
| Ollama         | Local LLM inference              |
| APScheduler    | Automated scheduling             |
| SQLite         | Persistent scheduler job storage |
| Slack Webhooks | Notifications                    |
| python-dotenv  | Environment configuration        |
| Requests       | Slack HTTP requests              |

---

# Prerequisites

Before using AutoPilot, install:

* Python 3
* Ollama
* An Ollama-compatible model
* A Gmail account
* A Gmail App Password
* A Slack workspace
* A Slack Incoming Webhook

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AutoPilot.git
```

Navigate into the project:

```bash
cd AutoPilot
```

Replace `YOUR_USERNAME` with the GitHub username that owns the repository.

---

## 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configuration

AutoPilot uses environment variables rather than hardcoding credentials.

Create a file called:

```text
.env
```

in the project root.

Example:

```env
OLLAMA_MODEL=mistral:latest

DATABASE_URL=sqlite:///jobs.sqlite

EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password

IMAP_SERVER=imap.gmail.com
IMAP_PORT=993

SLACK_WEBHOOK_URL=your_slack_webhook_url
```

### Configuration Variables

| Variable            | Description                         |
| ------------------- | ----------------------------------- |
| `OLLAMA_MODEL`      | Ollama model used for summarization |
| `DATABASE_URL`      | Database used by APScheduler        |
| `EMAIL_ADDRESS`     | Gmail account to monitor            |
| `EMAIL_PASSWORD`    | Gmail App Password                  |
| `IMAP_SERVER`       | Gmail IMAP server                   |
| `IMAP_PORT`         | Gmail IMAP port                     |
| `SLACK_WEBHOOK_URL` | Slack Incoming Webhook              |

---

# Gmail Setup

AutoPilot connects to Gmail using IMAP.

Use:

```env
IMAP_SERVER=imap.gmail.com
IMAP_PORT=993
```

## Gmail App Password

The application should use a Gmail App Password rather than the normal Gmail account password.

Set:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
```

Do not commit these values to GitHub.

---

# Ollama Setup

## 1. Install Ollama

Install Ollama for your operating system.

After installation, verify it:

```bash
ollama --version
```

## 2. Check Models

```bash
ollama list
```

## 3. Install a Model

For example:

```bash
ollama pull mistral:latest
```

## 4. Test the Model

```bash
ollama run mistral:latest
```

## 5. Configure AutoPilot

Set the same model name in `.env`:

```env
OLLAMA_MODEL=mistral:latest
```

The model must be available locally before AutoPilot can generate summaries.

---

# Slack Setup

AutoPilot uses a Slack Incoming Webhook.

Create or obtain a webhook for the Slack channel where the summaries should be delivered.

Add it to `.env`:

```env
SLACK_WEBHOOK_URL=your_slack_webhook_url
```

The application sends the generated summary to this webhook after successful processing.

---

# Running the Project

There are two ways to run AutoPilot.

## Manual Execution

Run:

```bash
python main.py
```

This immediately starts the complete pipeline.

The workflow is:

```text
main.py
   ↓
run_pipeline()
   ↓
Connect to Gmail
   ↓
Find unread emails
   ↓
Fetch emails
   ↓
Parse and clean
   ↓
Summarize with Ollama
   ↓
Save summary
   ↓
Send to Slack
```

---

# Scheduled Execution

To start the scheduler:

```bash
python run_scheduler.py
```

The scheduler starts APScheduler and registers the AutoPilot job.

The scheduled job calls:

```text
ai_job()
    ↓
run_pipeline()
```

The scheduler process must remain running for scheduled jobs to execute.

---

# Scheduler Configuration

The scheduler is configured in:

```text
scheduler/scheduler.py
```

## Every Minute

Useful for testing:

```python
scheduler.add_job(
    ai_job,
    trigger="interval",
    minutes=1,
    id="ai_job",
    replace_existing=True
)
```

## Every Day at 9:00 AM

```python
scheduler.add_job(
    ai_job,
    trigger="cron",
    hour=9,
    minute=0,
    id="ai_job",
    replace_existing=True
)
```

## Every Day at 1:34 PM

```python
scheduler.add_job(
    ai_job,
    trigger="cron",
    hour=13,
    minute=34,
    id="ai_job",
    replace_existing=True
)
```

## Every Tuesday at 12:20 PM

```python
scheduler.add_job(
    ai_job,
    trigger="cron",
    day_of_week="tue",
    hour=12,
    minute=20,
    id="ai_job",
    replace_existing=True
)
```

After changing the schedule, restart:

```bash
python run_scheduler.py
```

---

# Running Automatically on macOS

The scheduler normally requires:

```bash
python run_scheduler.py
```

to be running.

For a completely unattended setup on macOS, `run_scheduler.py` can be registered as a macOS LaunchAgent.

The LaunchAgent should execute:

```text
.venv/bin/python run_scheduler.py
```

from the project directory.

This allows macOS to start the scheduler automatically when the user logs in.

The computer must still be powered on for the scheduler to execute.

---

# Output and Logs

## Summaries

Generated summaries are stored in:

```text
summaries/
```

Example:

```text
summaries/
├── summary_20260810_090001.txt
└── summary_20260810_090125.txt
```

## Logs

Application logs are stored in:

```text
logs/
```

Logs contain information about:

* Scheduler execution
* Gmail connection
* Unread email count
* Email processing
* Retry attempts
* Ollama summarization
* Summary creation
* Slack notifications
* Errors
* Pipeline completion

---

# Error Handling and Reliability

AutoPilot includes error handling for the major external services.

## Gmail

The system handles connection and email-fetching failures.

## Ollama

The system handles summarization failures and model-loading delays.

## Slack

The system handles Slack notification failures.

## Retry Mechanism

Operations that may fail temporarily use retry attempts.

The general behaviour is:

```text
Attempt 1
   ↓
Failure
   ↓
Retry
   ↓
Attempt 2
   ↓
Failure
   ↓
Retry
   ↓
Attempt 3
   ↓
Success / Final Failure
```

Failures are recorded in the application logs.

---

# Testing

## Test 1 — Manual Pipeline

Send an email to the configured Gmail account and leave it unread.

Run:

```bash
python main.py
```

Verify that:

* The email is detected.
* The email is processed.
* A summary is generated.
* A summary file is created.
* A Slack notification is received.

---

## Test 2 — Multiple Emails

Send multiple test emails and leave them unread.

Run:

```bash
python main.py
```

AutoPilot should process each unread email individually.

---

## Test 3 — No Unread Emails

Run:

```bash
python main.py
```

when there are no unread emails.

The system should report that there are no unread emails and exit normally.

---

## Test 4 — Scheduled Pipeline

Configure a short interval for testing:

```python
trigger="interval",
minutes=1
```

Start:

```bash
python run_scheduler.py
```

Verify that the scheduler automatically runs the complete pipeline.

After testing, change the schedule to the desired production schedule.

---

# Troubleshooting

## `ollama` Command Not Found

Verify that Ollama is installed and available in the terminal.

```bash
ollama --version
```

---

## Model Not Found

Check:

```bash
ollama list
```

Then install the required model:

```bash
ollama pull mistral:latest
```

Ensure `.env` contains:

```env
OLLAMA_MODEL=mistral:latest
```

---

## Gmail Authentication Failure

Check:

```env
EMAIL_ADDRESS=...
EMAIL_PASSWORD=...
```

Make sure `EMAIL_PASSWORD` is a valid Gmail App Password.

Also verify:

```env
IMAP_SERVER=imap.gmail.com
IMAP_PORT=993
```

---

## No Unread Emails

This is not an error.

AutoPilot only processes unread emails.

Send a new test email and leave it unread before running the pipeline.

---

## Slack Notification Failure

Check that:

```env
SLACK_WEBHOOK_URL=...
```

contains a valid Slack Incoming Webhook URL.

---

## Scheduler Not Running

Start it with:

```bash
python run_scheduler.py
```

Make sure the process remains running.

---

# Security

This project is designed to be safe to publish publicly **provided that credentials and private data are excluded from the repository**.

## Never Commit

Do not commit:

```text
.env
```

or:

```text
jobs.sqlite
```

or generated logs and email summaries.

A recommended `.gitignore` is:

```gitignore
# Environment
.env

# Virtual environment
.venv/

# Python
__pycache__/
*.py[cod]

# Database
*.sqlite
*.db

# Logs
logs/

# Generated summaries
summaries/
```

Never put the following directly into Python source files:

* Gmail passwords
* Gmail App Passwords
* Slack Webhook URLs
* API keys
* Personal email contents

---

# Customisation

## Change the AI Model

Change:

```env
OLLAMA_MODEL=mistral:latest
```

to another locally installed Ollama model.

For example:

```env
OLLAMA_MODEL=llama3.2:3b
```

The model must first be installed:

```bash
ollama pull llama3.2:3b
```

---

## Change the Gmail Account

Update:

```env
EMAIL_ADDRESS=another_email@gmail.com
EMAIL_PASSWORD=another_app_password
```

---

## Change the Slack Channel

Update:

```env
SLACK_WEBHOOK_URL=another_webhook_url
```

---

## Change the Schedule

Modify the scheduler configuration in:

```text
scheduler/scheduler.py
```

Then restart:

```bash
python run_scheduler.py
```

---

# Future Improvements

Possible future enhancements include:

* Web-based configuration interface.
* Multiple Gmail account support.
* Richer email classification.
* Priority detection.
* Automatic email categorisation.
* Database-based summary history.
* Web dashboard for monitoring.
* Docker deployment.
* Cloud deployment.
* More advanced scheduling controls.
* Support for additional notification platforms.

These are optional extensions and are not required for the current system.

---

# Project Status

The core AutoPilot system is complete and operational.

Implemented functionality includes:

* [x] Gmail IMAP integration
* [x] Unread email detection
* [x] Multiple email processing
* [x] Email parsing
* [x] Email cleaning
* [x] Local Ollama summarization
* [x] Local summary storage
* [x] Slack notifications
* [x] Error handling
* [x] Retry mechanisms
* [x] Application logging
* [x] APScheduler integration
* [x] Persistent scheduler storage
* [x] Configurable scheduling
* [x] Manual execution
* [x] Automated scheduled execution
* [x] End-to-end testing
* [x] Handover documentation

---

# Quick Start

For an already-configured installation:

```bash
cd AutoPilot
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Run manually:

```bash
python main.py
```

Or start the scheduler:

```bash
python run_scheduler.py
```

---

# License

This project is available under the license specified in the repository.

If no license has been selected yet, add an appropriate license before distributing the project publicly.
