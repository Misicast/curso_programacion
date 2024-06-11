from typing import Callable

from pages.screen import Screen


class StartScreen(Screen):
    def __init__(self, on_key_pressed: Callable[[], None]) -> None:
        super().__init__()
        self.text = self.branding()
        self.on_key_pressed = on_key_pressed

    def render(self):
        print(self.text)
        input("Press key to continue")
        self.on_key_pressed()

    def branding(self) -> str:
        return """MISICAST

    Bienvenidos a nuestra tienda virtual local. Te ofrecemos productos
    para damas y caballeros, perfumes y carteras. Puedes realizar tus
    pedidos personalizados y lo traeremos por ti desde USA. Envios a 
    nivel nacional. Siguenos en @misicast_.

    Tel: +584141234567"""
