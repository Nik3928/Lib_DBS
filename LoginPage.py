import flet as ft
from AbstractView import AbstractView


class Login(AbstractView):
    def __init__(self):
        self.ltext = ft.Text("Log In", weight=ft.FontWeight.BOLD, size=24, text_align=ft.TextAlign.CENTER)
        self.login_field = ft.TextField(label="Login", width=300, height=50)
        self.password_field = ft.TextField(label="Password", width=300, height=50, password=True,
                                           can_reveal_password=True)
        self.error_lbl = ft.Text("", color="red")
        self.log_button = ft.ElevatedButton("Log In", height=50, width=120)
        self._controls: list[ft.Control] = [self.ltext, self.login_field, self.password_field, self.log_button, self.error_lbl]

    @property
    def controls(self):
        """ :returns controls in view"""
        return self._controls

    def build(self):
        """ :returns view object """
        return ft.View(
            "/",
            self.controls,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )


if __name__ == '__main__':
    def main(page: ft.Page):
        page.views.append(Login().build())
        page.update()


    ft.app(target=main)
