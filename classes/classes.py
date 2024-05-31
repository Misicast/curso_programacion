# Tipos de datos basicos
# Number: int, float
# Text: str
# Boolean(True/False): bool
# Iterators: list, tuple, dict, set
# None: NoneType
# Tipos de datos personalizados:
# Date: Datetime
# Etc...
# Ejemplo 1: Representar mediates class. Fabrica de carros


from math import acos, pi, sqrt


class Fabrica:
    def __init__(self) -> None:
        self.name = "Fabrica 133"
        self.location = "mi casa"


class Carro:
    def __init__(self) -> None:
        self.marca = "Ford"
        self.color = "verde"
        self.modelo = "Explorer"
        self.year = "2022"
        self.placa = "ABC123"
        self.a_c = True
        self.km = 0


fab_1 = Fabrica()
print(fab_1.name, fab_1.location)
carro_1 = Carro()
print(
    carro_1.marca,
    carro_1.color,
    carro_1.modelo,
    carro_1.year,
    carro_1.placa,
    carro_1.a_c,
    carro_1.km,
)


# Clases y objetos
# Clases es una plantilla
# Objetos es elemento defindo por una plantilla
class Arbol:
    def __init__(self, name: str, specie: str) -> None:
        self.name = name
        self.specie = specie


araguaney_de_mi_casa = Arbol(name="araguaney", specie="amarilla")
manzanero = Arbol(name="manzanero", specie="verde")

print(araguaney_de_mi_casa.name, araguaney_de_mi_casa.specie)
print(manzanero.name, manzanero.specie)

# Uso de clases y uso de los objetos


# - Encapsular datos o acciones/logica
# - Representar elementos o fenomenos fisicos
## Elementos fiscos
class Mascota:
    def __init__(self, name: str, owner: str) -> None:
        self.name = name
        self.owner = owner

    def caminar(self):
        print("estoy caminando " + self.owner)


## Fenomeno fisico
class Point:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z


class Vector:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2

    def magnitud(self):
        return sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)

    def direccion(self):
        return acos((self.p2.x - self.p1.x) / self.magnitud()) * (180 / pi)


class Velocidad:
    def __init__(self, vector: Vector, time: float) -> None:
        self.vector = vector
        self.t = time

    def calcular(self) -> float:
        return (self.vector.p2.x - self.vector.p1.x) / self.t


Tomy = Mascota(name="Tomy", owner="Yo")
Tomy.caminar()
Vicky = Mascota(name="Vicky", owner="Lennis")
Vicky.caminar()

point_a = Point(x=0, y=0, z=0)
point_b = Point(x=1, y=1, z=1)
vector_a_b = Vector(p1=point_a, p2=point_b)
print("Vector AB, magnitud: " + str(vector_a_b.magnitud()))
print("Vector AB, direccion: " + str(vector_a_b.direccion()))
velocidad_a_b = Velocidad(vector=vector_a_b, time=2)
print("Velocidad es de: " + str(velocidad_a_b.calcular()))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}(age={self.age})"

    def __len__(self):
        return self.age

    def __add__(self, obj):
        if type(obj) is Person:
            return self.age + obj.age
        return self.age


def personToStr(person):
    return f"{person.name}(age={person.age})"
