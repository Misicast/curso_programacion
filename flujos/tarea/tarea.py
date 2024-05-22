from typing import Any, List

import flujos.tarea.types as typings


def velocidad(punto_a: typings.Punto, punto_b: typings.Punto, tiempo: float, at) -> float:
    return (punto_b.x-punto_a.x)/tiempo

def mapper(data: dict) -> typings.DatosDeDiccionario:
    return typings.DatosDeDiccionario(name=data["name"],lastname=data["lastname"],age=data["age"])

def total_to_pay(products: List[typings.Product]) -> float:
    precios=[]
    for product in products:
        precios.append(product.price)
        return sum(precios)*1,16
    


def most_sold_products(products: List[typings.Product]) -> List[typings.Product]:
    def sortqtysold(products:typings.Product):
        return products.qty_sold
    products.sort(key=sortqtysold)
    products.reverse()
    mostsoldproduct=[]
    for index in range (0,5)
    mostsoldproduct.append(products[index])
    return mostsoldproduct


def most_repited_failures(failures: List[typings.Failures]) -> List[typings.Failures]:
    electrical=[]
    mechanical=[]
    network=[]
    service=[]
    other=[]
    for failure in failures:
        if failure.name=="electrical":
            electrical.append(failure)
        if failure.name=="mechanical":
            mechanical.append(failure)
        if failure.name=="network":
            network.append(failure)
        if failure.name=="service":
            service.append(failure)  
        if failure.name=="other":
            other.append(failure) 

    fallas=[
        {"failures" :typings.Failures(name="electrical"),"qty":len(electrical)}
        {"failures" :typings.Failures(name="mechanical"),"qty":len(mechanical)}
        {"failures" :typings.Failures(name="network"),"qty":len(network)}
        {"failures" :typings.Failures(name="service"),"qty":len(service)}
        {"failures" :typings.Failures(name="other"),"qty":len(other)}
    ]
    def sortqtysold(products:typings.Product):
        return fallas ["qty"]
    fallas.sort(key=sortqtysold)
    fallas.reverse()
    mostrepitedfailures=[]
    for index in range (0,3):
        mostrepitedfailures.append(fallas[index]["failure"])
        return mostrepitedfailures
    


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



