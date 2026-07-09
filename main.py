from llm.ollama_client import ask_model


def main():
    reply = ask_model("Say hello in one sentence.")
    print(reply)


if __name__ == "__main__":
    main()