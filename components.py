import flet as ft
from theme import *


def bubble(text, is_user=False):

    return ft.Container(
        content=ft.Text(
            text,
            color=TEXT,
            selectable=True,
        ),

        bgcolor=USER_BUBBLE if is_user else AI_BUBBLE,

        border_radius=20,

        padding=15,

        margin=10,

        width=500,

        alignment=(
            ft.alignment.center_right
            if is_user
            else ft.alignment.center_left
        ),
    )