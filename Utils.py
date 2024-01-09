from __future__ import annotations
from hashlib import sha256
import flet as ft
import db_wrap as db
from User import User
import random


class Utils:
    @staticmethod
    def check_text_fields_not_emtpy(controls: list[ft.TextField]) -> bool:
        """ Checks if any TextField is empty """
        for control in controls:
            if not control.value:
                control.focus()
                return False
        return True

    @staticmethod
    def check_system_user(connection: db.Connection, username: str, password: str) -> User | None:
        """ Try to find user with such data """
        # try:
        res = connection.query_c(f"SELECT * FROM dbs_users WHERE name='{username}'")
        if res and res[0][2] == sha256(password.encode()).hexdigest():
            res = res[0]
            return User(res[0], res[1], [])
        return

    @staticmethod
    def permission_check(permissions: list[str], user: User) -> bool:
        """ :returns True if user have those permissions """
        return all([permission in user.permissions or permission == '*' for permission in permissions])

    @staticmethod
    def gen_lc_number():
        """ Generates 8digit library card number """
        return random.randint(10000000, 99999999)
