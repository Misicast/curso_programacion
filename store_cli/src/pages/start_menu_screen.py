from typing import Callable

from pages.screen import Screen


class StartMenuScreen(Screen):
    def __init__(self, on_option_selected: Callable[[int], None]) -> None:
        super().__init__()
        self.menu = self.start_menu()
        self.on_option_selected = on_option_selected

    def render(self):
        try:
            option = int(input(self.menu))
            if option > 4 or option < 1:
                option = 4
            self.on_option_selected(option)
        except ValueError:
            self.on_option_selected(4)

    def start_menu(self) -> str:
        return """Ingresa una las opciones:

(1) Ver catalogo
(2) Crear Orden de compra 
(3) Ver orden de compra 
(4) Salir

Seleccion: """
