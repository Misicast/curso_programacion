import datetime

from more_itertools import quantify

# Numerico [int , float]
print("Numeros")
print(type(5))
print(type(5.0))
# Texto [str]
print("Texto")
print(type("T"))
print(type("lo mas larga posible"))
# List(ordenada)
print("Lista")
lista = [1, 2, 2, 3, 3]
print(lista)
print(type(lista))
print(lista[2])
# Set (no ordenado)
print("Sets")
conjunto_cerrado = {1, 2, 2, 3, 3}
print(conjunto_cerrado)
print(type(conjunto_cerrado))
# Diccionarios(posicion fija no ordenada)
print("Diccionarios")
diccionario = {"uno": 2, "pepe": 85, "5": "otra cosa"}
print(diccionario)
print(diccionario["uno"])
print(type(diccionario))
# Tuplas(ordenadas, inmutables)
print("Tuple")
tupla = (15, 75, "Texto")
print(tupla)
print(tupla[2])
print(type(tupla))
# Datetime
date = datetime.datetime.now()
print("Date")
print(date)
print(type(date))

# Tipo de dato personalizado
print("Dato personalizado")


# Esto es un mega error porque no es mantenible
# nombres_productos = ["colonia A", "colonia B"]
# cantidad_producto = ["100ml"]
# precio_producto = [25, 10]
# unida_precio_producto = ["USD"]
class Producto:
    def __init__(self, name, quantity, price, unit_price) -> None:
        self.name = name
        self.quantity = quantity
        self.price = price
        self.unit_price = unit_price


lista_productos = [
    Producto(name="colinaA", quantity="100ml", price=25, unit_price="USD"),
    Producto(name="colinaB", quantity="150ml", price=2, unit_price="EUR"),
]
print(type(lista_productos[0]))
print(
    lista_productos[0].name,
    lista_productos[0].price,
    lista_productos[0].quantity,
    lista_productos[0].unit_price,
)
# ---------------------------------------
print("Acciones/metodos")
# Numerico [int , float]
print("Numeros")
a = 5
print(a.bit_count())
f = 5.02
print(f.is_integer())
# Texto [str]
print("Texto")
texto = "algun texto cualquiera"
print(texto.capitalize())
print(texto.count("a"))
print(texto.center(50))
print(texto.endswith("iera"))
print(texto.startswith("iera"))
print(texto.find("g"))
# List(ordenada)
print("Lista")
lista = [1, 2, 4, 3, 3]
print(lista[2])
print(lista.append(4))
print(lista.count(2))
print(lista.pop())
print(lista)
print(lista.reverse())
print(lista)
print(lista.sort())
print(lista)
# Set (no ordenado)
print("Sets")
conjunto_cerrado = {1, 2, 2, 3, 3}
print(conjunto_cerrado.pop())
# Diccionarios(posicion fija no ordenada)
print("Diccionarios")
diccionario = {"uno": 2, "pepe": 85, "5": "otra cosa"}
print(diccionario.pop("uno"))
print(diccionario.items())
print(diccionario.keys())
# Tuplas(ordenadas, inmutables)
print("Tuple")
tupla = (15, 75, "Texto")
print("Dato personalizado")
prodA = Producto(name="A", price="25", quantity="8ml", unit_price="BTC")
