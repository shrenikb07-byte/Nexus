import requests

from memory import add_message, get_conversation
from time_tools import get_current_time
from long_term_memory import remember, recall

URL = "http://127.0.0.1:1234/v1/chat/completions"


def chat(user):

    current_time = get_current_time()

    # Load long-term memory
    name = recall("name")

    memory_info = ""

    if name:
        memory_info += f"The user's name is {name}.\n"

    messages = [
        {
            "role": "system",
            "content": f"""
You are Nexus, a friendly AI assistant.

Current date and time:
{current_time}

Known information:
{memory_info}

Rules:
- Use the current date and time above.
- Call the user "bro".
- Be friendly and helpful.
- If you know the user's name, use it naturally.
"""
        }
    ]

    # Add previous conversation
    messages.extend(get_conversation())

    # Add current message
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

    # -------------------------
    # Long-term memory
    # -------------------------

    if "my name is" in user.lower():
        try:
            name = user.split("is", 1)[1].strip()
            remember("name", name)
        except Exception:
            pass

    # Save conversation
    add_message("user", user)
    add_message("assistant", reply)

    return reply