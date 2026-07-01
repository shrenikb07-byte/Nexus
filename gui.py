import flet as ft
from ai import chat


def main(page: ft.Page):
    page.title = "🤖 Nexus"
    page.window.width = 900
    page.window.height = 700
    page.theme_mode = ft.ThemeMode.DARK

    # Chat area
    chat_view = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    # Input box
    message = ft.TextField(
        hint_text="Type your message...",
        expand=True,
    )

    # Function when Send is pressed
    def send_message(e):

        if message.value.strip() == "":
            return

        user_text = message.value

        # Show user's message
        chat_view.controls.append(
            ft.Text(f"👤 You: {user_text}")
        )

        page.update()

        # Get AI response
        reply = chat(user_text)

        # Show AI response
        chat_view.controls.append(
            ft.Text(f"🤖 Nexus: {reply}")
        )

        message.value = ""
        page.update()

    # Send button
    send_button = ft.ElevatedButton(
        "Send",
        on_click=send_message
    )

    # Press Enter to send
    message.on_submit = send_message

    page.add(
        ft.Column(
            [
                ft.Text(
                    "🤖 Nexus",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                ),
                chat_view,
                ft.Row(
                    [
                        message,
                        send_button,
                    ]
                ),
            ],
            expand=True,
        )
    )


ft.app(target=main)