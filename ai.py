import requests

from memory import add_message, get_conversation
from time_tools import get_current_time

URL = "http://127.0.0.1:1234/v1/chat/completions"

def chat(user):

    current_time = get_current_time()

    messages = [
        {
            "role": "system",
            "content": f"""
You are Nexus.

Current date and time:
{current_time}

Rules:
- Use the current date and time above.
- Call the user 'bro'.
- Be friendly.
"""
        }
    ]

    messages.extend(get_conversation())

    messages.append(
        {
            "role": "user",
            "content": user
        }
    )

    response = requests.post(
        URL,
        json={
            "model": "meta-llama-3.1-8b-instruct",
            "messages": messages
        }
    )

    reply = response.json()["choices"][0]["message"]["content"]

    add_message("user", user)
    add_message("assistant", reply)

    return reply