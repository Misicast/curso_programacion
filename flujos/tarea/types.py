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


class Email:
    def __init__(
        self,
        by: str,
        to: str,
        subject: str,
        content: str,
        is_favorite: bool = False,
        is_urgent: bool = False,
    ) -> None:
        self.by = by
        self.to = to
        self.susbject = subject
        self.is_favorite = is_favorite
        self.is_urgent = is_urgent
        self.content = content


class ProductCategory:
    def __init__(
        self,
        name: Literal["perfume", "bisuteria", "carteras", "zapatos", "gorras"],
        product_qty_sold: int,
        total_amount_sold: float,
    ) -> None:
        self.name = name
        self.product_qty_sold = product_qty_sold
        self.total_amount_sold = total_amount_sold


class LanguageDictionary:
    def __init__(self):
        self.__language__ = {}

    def add(self, word: str, translation: str) -> "LanguageDictionary":
        """
        Add word and translation
        """
        self.__language__[word] = translation
        return self

    def __getattribute__(self, name: str) -> str:
        return self.__language__[name]

    def __len__(self) -> int:
        return len(self.__language__)

    def __contains__(self, key: object) -> bool:
        return key in self.__language__


class SystemLanguage:
    en_es = LanguageDictionary()
    es_en = LanguageDictionary()
