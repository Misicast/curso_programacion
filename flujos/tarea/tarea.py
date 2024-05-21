from typing import Any, List

import flujos.tarea.types as typings


def velocidad(punto_a: typings.Punto, punto_b: typings.Punto, tiempo: float, at) -> float:
    raise NotImplemented()

def mapper(data: dict) -> typings.DatosDeDiccionario:
    raise NotImplemented()

def total_to_pay(products: List[typings.Product]) -> float:
    raise NotImplemented()


def most_sold_products(products: List[typings.Product]) -> List[typings.Product]:
    raise NotImplemented()


def most_repited_failures(failures: List[typings.Failures]) -> List[typings.Failures]:
    raise NotImplemented()

# Parte II

def maximun(numbers: List[float]) -> float:
    return max(numbers)

def count_words(words: List[str]) -> dict[str, int]:
    conteo={}
    for  word in words:
        if  not word in conteo:
            conteo[word] = words.count(word)
    return conteo



def get_favorites(emails: List[typings.Email]) -> List[typings.Email]:
    fav = []
    for email in emails:
        if email.is_favorite:
            fav.append(email)
    return fav



def most_consumed_categories(categories: List[typings.ProductCategory]) -> List[typings.ProductCategory]:
    def mostconsumedcategories(categories:typings.ProductCategory):
        return categories.qty_sold
    categories.sort(key=mostconsumedcategories)
    categories.reverse()

    
    

def most_amount_consumed_category(categories: List[typings.ProductCategory]) -> List[typings.ProductCategory]:
    def mostamountconsumedcategory(categories:typings.ProductCategory):
        return categories.total_amount_sold
    categories.sort(key=mostamountconsumedcategory)
    categories.reverse()


def most_consumed_categories_percent(categories: List[typings.ProductCategory]) -> dict[str, float]:
    product_qty_sold=[]
    for product in categories:
        product_qty_sold.append(product.product_qty_sold)
    m=sum(product_qty_sold)
    consumo={}
    for category in categories:
        if category.name in consumo:
            consumo[category.name]=category.product_qty_sold/m + consumo[category.name]
        else:
            consumo[category.name]=category.product_qty_sold/m
    return consumo



