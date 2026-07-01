import requests
from datetime import datetime
URL = "http://127.0.0.1:1234/v1/chat/completions"

print("🤖 Shrenik AI")
print("Type 'exit' to quit.\n")

current_time = datetime.now().strftime("%A, %d %B %Y | %I:%M:%S %p")

conversation = [
    {
        "role": "system",
        "content": f"""You are Shrenik AI.

Current date and time:
{current_time}

Always use this as the current time.
Call the user 'bro' and be friendly.
"""
    }
]

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    conversation.append(
        {
            "role": "user",
            "content": user
        }
    )

    response = requests.post(
        URL,
        json={
            "model": "meta-llama-3.1-8b-instruct",
            "messages": conversation
        }
    )

    reply = response.json()["choices"][0]["message"]["content"]

    conversation.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    print("\nAI:", reply)
    print()