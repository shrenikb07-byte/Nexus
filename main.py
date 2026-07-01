from ai import chat

print("🤖 Nexus")
print("Type 'exit' to quit.\n")

while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    reply = chat(user)

    print("\nNexus:", reply)
    print()