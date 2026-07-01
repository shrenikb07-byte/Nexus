import flet as ft

def main(page: ft.Page):
    page.title = "🤖 Nexus"
    page.window.width = 900
    page.window.height = 700
    page.theme_mode = ft.ThemeMode.DARK

    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    message = ft.TextField(
        hint_text="Type a message...",
        expand=True,
    )

    send = ft.ElevatedButton("Send")

    page.add(
        ft.Column(
            [
                ft.Text(
                    "🤖 Nexus",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                ),
                chat,
                ft.Row(
                    [
                        message,
                        send,
                    ]
                ),
            ],
            expand=True,
        )
    )

ft.app(target=main)