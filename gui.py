import flet as ft
from ai import chat
from theme import *
from components import bubble


def main(page: ft.Page):

    page.title = "🤖 Nexus"
    page.window.width = 1200
    page.window.height = 800

    page.theme_mode = ft.ThemeMode.DARK
    
    page.bgcolor = BACKGROUND
    page.padding = 0

    # ---------------------------
    # Header
    # ---------------------------

    header = ft.Container(
        bgcolor=SIDEBAR,
        padding=20,
        content=ft.Row(
            [
                ft.Text(
                    "🤖 Nexus",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=TEXT,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
    )

    # ---------------------------
    # Chat Area
    # ---------------------------

    chat_view = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    chat_container = ft.Container(
        expand=True,
        padding=20,
        content=chat_view,
    )

    # Welcome message

    chat_view.controls.append(
        bubble("👋 Hello bro!\n\nWelcome to Nexus.\nAsk me anything.")
    )

    # ---------------------------
    # Input
    # ---------------------------

    message = ft.TextField(
        hint_text="Ask Nexus anything...",
        border_radius=30,
        filled=True,
        bgcolor=INPUT,
        border_color=INPUT,
        color=TEXT,
        expand=True,
    )

    def send_message(e):

        if message.value.strip() == "":
            return

        user = message.value

        chat_view.controls.append(
            bubble(user, True)
        )

        page.update()

        reply = chat(user)

        chat_view.controls.append(
            bubble(reply)
        )

        message.value = ""

        page.update()

    message.on_submit = send_message

    send_button = ft.ElevatedButton(
        "Send",
        on_click=send_message,
        bgcolor=PRIMARY,
        color="white",
    )

    input_bar = ft.Container(
        bgcolor=SIDEBAR,
        padding=20,
        content=ft.Row(
            [
                message,
                send_button,
            ]
        ),
    )

    # ---------------------------
    # Sidebar
    # ---------------------------

    sidebar = ft.Container(
        width=230,
        bgcolor=SIDEBAR,
        padding=20,
        content=ft.Column(
            [
                ft.Text(
                    "💬 Chats",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=TEXT,
                ),

                ft.Divider(),

                ft.ElevatedButton(
                    "+ New Chat",
                    width=180,
                ),

                ft.Divider(),

                ft.Text(
                    "Version 2.1",
                    color=TEXT_LIGHT,
                ),
            ]
        ),
    )

    # ---------------------------
    # Main Area
    # ---------------------------

    main_area = ft.Column(
        [
            header,
            chat_container,
            input_bar,
        ],
        expand=True,
    )

    page.add(

        ft.Row(
            [
                sidebar,
                main_area,
            ],
            expand=True,
        )

    )


ft.app(target=main)