
# AutoPilot — Handover Document

## 1. Project Setup

Open a terminal and go to the project folder:

cd path/to/AutoPilot
````

Create the virtual environment:

python3 -m venv .venv
```

Activate it:

source .venv/bin/activate
```

Install the required packages:

pip install -r requirements.txt
```

---

## 2. Configure the `.env` File

Create a `.env` file in the main project folder.

Add:

OLLAMA_MODEL=mistral:latest

DATABASE_URL=sqlite:///jobs.sqlite

EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password

IMAP_SERVER=imap.gmail.com
IMAP_PORT=993

SLACK_WEBHOOK_URL=your_slack_webhook_url
```

Replace the placeholder values with the correct details.

### Gmail

Use a Gmail App Password for:

EMAIL_PASSWORD=
```

Do not use the normal Gmail account password.

### Ollama

Check the installed models:

ollama list
```

The model name in `.env` must match an installed model.

For example:

OLLAMA_MODEL=mistral:latest
```

### Slack

Add the Slack Incoming Webhook URL:

SLACK_WEBHOOK_URL=your_slack_webhook_url
```

---

## 3. Run the Pipeline Manually

Activate the virtual environment:

source .venv/bin/activate
```

Run:

python main.py
```

This will:

1. Connect to Gmail.
2. Find unread emails.
3. Fetch and clean the emails.
4. Summarize them using Ollama.
5. Save the summaries.
6. Send the summaries to Slack.

---

## 4. Run the Scheduler

To run AutoPilot automatically:

python run_scheduler.py
```

Keep this terminal/process running.

The scheduler will automatically run the AutoPilot pipeline according to the configured schedule.

---

## 5. Change the Schedule

Open:

scheduler/scheduler.py
```

### Every Minute

scheduler.add_job(
    ai_job,
    trigger="interval",
    minutes=1,
    id="ai_job",
    replace_existing=True
)
```

### Every Day at 9:00 AM

scheduler.add_job(
    ai_job,
    trigger="cron",
    hour=9,
    minute=0,
    id="ai_job",
    replace_existing=True
)
```

### Every Tuesday at 12:20 PM

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

After changing the schedule, restart the scheduler:

python run_scheduler.py
```

---

## 6. Important Files

| File/Folder              | Purpose                                  |
| ------------------------ | ---------------------------------------- |
| `.env`                   | Configuration and credentials            |
| `main.py`                | Runs the pipeline manually               |
| `pipeline.py`            | Main email processing workflow           |
| `run_scheduler.py`       | Starts the scheduler                     |
| `scheduler/scheduler.py` | Configures the schedule                  |
| `scheduler/jobs.py`      | Runs the scheduled pipeline              |
| `email_service/`         | Gmail connection and email processing    |
| `llm_service/`           | Ollama summarization and summary storage |
| `slack_service/`         | Slack message formatting and sending     |
| `summaries/`             | Saved email summaries                    |
| `logs/`                  | Application logs                         |

---

## 7. Common Commands

### Activate the virtual environment

source .venv/bin/activate
```

### Run manually

python main.py
```

### Run automatically

python run_scheduler.py
```

### Check Ollama models

ollama list
```

### Test an Ollama model

ollama run mistral:latest
```

---

## 8. Important Notes

* The `.env` file must be present for the system to work.
* The Ollama model configured in `.env` must be installed.
* A Gmail App Password must be used.
* The Slack Webhook URL must be valid.
* The scheduler process must remain running for scheduled jobs to execute.
* After changing the schedule, restart `run_scheduler.py`.

```
```
