import json
import urllib.request
import urllib.error


OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "qwen2.5:3b"


def ask_ai(prompt):
    """
    Send a prompt to Ollama and return the AI response.
    """

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
    }

    data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        OLLAMA_URL,
        data=data,
        headers={"Content-Type": "application/json"},
    )

    try:
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode())

        return result["response"]

    except urllib.error.URLError:
        return "Unable to connect to Ollama."

    except Exception as error:
        return f"Error: {error}"
