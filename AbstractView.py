import flet as ft
import abc


class AbstractView:
    @abc.abstractmethod
    def build(self) -> ft.View:
        pass

    @property
    @abc.abstractmethod
    def controls(self) -> list[ft.Control]:
        pass
