from typing import List

import flujos.tarea.types as typings


def velocidad(punto_a: typings.Punto, punto_b: typings.Punto, tiempo: float) -> float:
    return (punto_b.x - punto_a.x) / tiempo


def mapper(data: dict) -> typings.DatosDeDiccionario:
    return typings.DatosDeDiccionario(
        name=data["name"], lastname=data["lastname"], age=data["age"]
    )


def total_to_pay(products: List[typings.Product]) -> float:
    precios = []
    for product in products:
        precios.append(product.price)
    return sum(precios) * 1.16


def most_sold_products(products: List[typings.Product]) -> List[typings.Product]:
    def sortqtysold(products: typings.Product):
        return products.qty_sold

    products.sort(key=sortqtysold)
    products.reverse()
    mostsoldproduct = []
    for index in range(0, 5):
        mostsoldproduct.append(products[index])
    return mostsoldproduct


def most_repited_failures(failures: List[typings.Failures]) -> List[typings.Failures]:
    electrical = []
    mechanical = []
    network = []
    service = []
    other = []
    for failure in failures:
        if failure.name == "electrical":
            electrical.append(failure)
        if failure.name == "mechanical":
            mechanical.append(failure)
        if failure.name == "network":
            network.append(failure)
        if failure.name == "service":
            service.append(failure)
        if failure.name == "other":
            other.append(failure)

    fallas = [
        {"failure": typings.Failures(name="electrical"), "qty": len(electrical)},
        {"failure": typings.Failures(name="mechanical"), "qty": len(mechanical)},
        {"failure": typings.Failures(name="network"), "qty": len(network)},
        {"failure": typings.Failures(name="service"), "qty": len(service)},
        {"failure": typings.Failures(name="other"), "qty": len(other)},
    ]

    def sort_by_qty(failure_detail: dict):
        return failure_detail["qty"]

    fallas.sort(key=sort_by_qty)
    fallas.reverse()
    mostrepitedfailures = []
    for index in range(0, 3):
        mostrepitedfailures.append(fallas[index]["failure"])
    return mostrepitedfailures


# ------------
# Parte II
# ------------


def maximun(numbers: List[float]) -> float:
    return max(numbers)


def count_words(words: List[str]) -> dict[str, int]:
    conteo = {}
    words_in_lower = []
    for word in words:
        words_in_lower.append(word.lower())
    for word in words:
        if not word.lower() in conteo:
            conteo[word.lower()] = words_in_lower.count(word.lower())
    return conteo


def get_favorites(emails: List[typings.Email]) -> List[typings.Email]:
    fav = []
    for email in emails:
        if email.is_favorite:
            fav.append(email)
    return fav


def most_consumed_categories(
    categories: List[typings.ProductCategory],
) -> List[typings.ProductCategory]:
    def mostconsumedcategories(category: typings.ProductCategory):
        return category.product_qty_sold

    categories.sort(key=mostconsumedcategories)
    categories.reverse()
    return categories


def most_amount_consumed_category(
    categories: List[typings.ProductCategory],
) -> List[typings.ProductCategory]:
    def mostamountconsumedcategory(category: typings.ProductCategory):
        return category.total_amount_sold

    categories.sort(key=mostamountconsumedcategory)
    categories.reverse()
    return categories


def most_consumed_categories_percent(
    categories: List[typings.ProductCategory],
) -> dict[str, float]:
    product_qty_sold = []
    for product in categories:
        product_qty_sold.append(product.product_qty_sold)
    m = sum(product_qty_sold)
    consumo = {}
    for category in categories:
        if category.name in consumo:
            consumo[category.name] = (
                category.product_qty_sold / m + consumo[category.name]
            )
        else:
            consumo[category.name] = category.product_qty_sold / m
    return consumo


# ------------
# Parte III
# ------------


def get_avatar_initials(names: List[str]) -> List[str]:
    initials = []
    for full_name in names:
        full_name_splited = full_name.split(" ")
        first_name = full_name_splited[0]
        last_name = full_name_splited[1]
        initialfn = first_name[0]
        initialln = last_name[0]
        initials.append(initialfn + initialln)
    return initials


def get_id_from_url(url: str) -> str:
    id = url.split("/")[1]
    return id


def search_products(
    products: List[typings.Product], search: str
) -> List[typings.Product]:
    searchproduct = []
    for product in products:
        if search.lower() in product.name.lower():
            searchproduct.append(product)
    return searchproduct


def translate(
    lang: typings.LanguageDictionary, word: str, default_translation: str
) -> str:
    if word in lang:
        return lang[word]
    else:
        lang.add(word, default_translation)
        return default_translation


def fizz_buzz(num: int) -> str:
    if num % 2 == 0 and num % 5 == 0:
        return "fizz-buzz"
    if num % 2 == 0:
        return "fizz"
    if num % 5 == 0:
        return "buzz"
    else:
        return "game over"
