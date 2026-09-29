class EmailConnectionError(Exception):
    """Raised when Gmail connection fails."""
    pass


class EmailFetchError(Exception):
    """Raised when email fetching fails."""
    pass


class SummarizationError(Exception):
    """Raised when Ollama summarization fails."""
    pass

class SlackNotificationError(Exception):
    """Raised when Slack notification fails."""
    pass