from __future__ import annotations

import flet as ft

import LoginPage
import config
import db_wrap as db
from User import User
from Utils import Utils

USER: User | None = None


def main(page: ft.Page):
    def login():
        def log_button_pressed(e: ft.ControlEvent):
            if Utils.check_text_fields_not_emtpy([view.login_field, view.password_field]):
                global USER
                USER = Utils.check_system_user(connection, view.login_field.value, view.password_field.value)
                if USER:
                    main_interface(e)
                else:
                    view.error_lbl.value = "Incorrect login or password"
                    page.update()

        view = LoginPage.Login()
        view.log_button.on_click = log_button_pressed
        page.views.clear()
        page.views.append(view.build())
        page.update()

    def main_interface(e: ft.ControlEvent):
        page.views.append(ft.View("/"))
        page.update()
        print(USER)

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.INDIGO,
            primary_container=ft.colors.INDIGO_500
        )
    )
    page.title = "Home Work"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    err_text = ft.Text(value="", color="red", text_align=ft.TextAlign.CENTER)
    page.add(err_text)

    connection: db.Connection | None = None
    try:
        connection = db.Connection(config.HOST, config.DB_USER, config.DB_PASSWORD, config.DB_NAME, config.PORT)
        login()
    except Exception as exc:
        err_text.value = "Can't connect to database, check your Internet connection or ask admin help"
        print(exc)
        page.update()
        return


if __name__ == '__main__':
    ft.app(target=main)
