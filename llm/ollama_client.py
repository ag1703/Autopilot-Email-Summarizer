import ollama

from config.settings import OLLAMA_MODEL


def ask_model(prompt: str) -> str:
    """
    Sends a prompt to the local Ollama model
    and returns only the generated text.
    """
    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]