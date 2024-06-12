
from typing import Callable
from pages.screen import Screen


class ProductList(Screen):
    def __init__(self, on_option_selected:Callable[[int],None]) -> None:
        super().__init__()
        self.text=self.categories()
        self.on_option_seleted=on_option_selected

    def render(self):
        try:
            option=int(input(self.text))
            if option > 5 or option < 1:
                option=5
            self.on_option_seleted(option)
        except ValueError:
            self.on_option_seleted(5)

    
    def categories(self):
        return """Ingresa una de las opciones:
(1) Perfumes Caballeros
(2) Perfumes de Damas
(3) Carteras Originales
(4) Accesorios
(5) Regresar

Seleccion: """    