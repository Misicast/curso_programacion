from typing import Literal


class Punto:
    def __init__(self, x: float) -> None:
        self.x = x


class DatosDeDiccionario:
    def __init__(self, name: str, lastname: str, age: int) -> None:
        self.name = name
        self.lastname = lastname
        self.age = age


class Product:
    def __init__(self, name: str, price: float, qty_sold: int = 0) -> None:
        self.name = name
        self.price = price
        self.qty_sold = qty_sold


class Failures:
    def __init__(
        self,
        name: Literal["electrical", "mechanical", "network", "service", "other"],
    ) -> None:
        self.name = name
