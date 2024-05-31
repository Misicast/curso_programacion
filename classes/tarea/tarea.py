# 1
class CarFactory:
    def __init__(
        self,
        name,
        marca,
        ubicacion,
    ):
        self.name = name
        self.marca = marca
        self.ubicacion = ubicacion

    def fabricar(self, modelo, tipo, ac, ce, añofab):
        return Car(
            modelo=modelo, tipo=tipo, ac=ac, ce=ce, añofab=añofab, marca=self.marca
        )


class Car:
    def __init__(self, modelo, tipo, ac, ce, añofab, marca):
        self.modelo = modelo
        self.tipo = tipo
        self.ac = ac
        self.ce = ce
        self.añofab = añofab
        self.marca = marca


# 2
class Folder:
    def __init__(self, carpetas, archivos, nombrec, ubicacion):
        self.nombrec = nombrec
        self.ubicacion = ubicacion
        self.carpeta = carpetas
        self.archivo = archivos


class File:
    def __init__(self, extension, nombrea, fcreacion, ubicacion):
        self.extension = extension
        self.nombrea = nombrea
        self.fcreacion = fcreacion
        self.ubicacion = ubicacion


# 3
# gen_fib.next() [n1=0,n2=1] ->[n1=1, n2=1]
# gen_fib.next() [n1=1, n2=1] -> [n1=1, n2=2]
# gen_fib.next() [n1=1, n2=2] -> [n1=2, n2=3]
# gen_fib.next() [n1=2, n2=3] -> [n1=3, n2=5]
# gen_fib.next() [n1=3, n2=5] -> [n1=5, n2=8]
# gen_fib.next() [n1=5, n2=8] -> [n1=8, n2=13]
class FibonacciGen:
    def __init__(self):
        self.n1 = 0
        self.n2 = 1
        self.intentos = 10

    def generar(self) -> int:
        fib = self.n1 + self.n2
        self.n1 = self.n2
        self.n2 = fib
        self.intentos -= 1
        return fib  # decremento

    def puede_generar(self):
        return self.intentos > 0


# 4
class TelephoneCarrierCentral:
    def __init__(self, name, clientes) -> None:
        self.clientes = clientes
        self.name = name

    def registrar(self, cliente):
        self.clientes.append(cliente)

    def notificar(self, mensaje):
        for cliente in self.clientes:
            cliente.notificar(mensaje)

    def removercliente(self, cliente):
        filtered_list = []
        for clientex in self.clientes:
            if clientex.numero == cliente.numero:
                continue
            else:
                filtered_list.append(clientex)
        self.clientes = filtered_list

        # help


class TelephoneClient:
    def __init__(self, nombre, numero) -> None:
        self.nombre = nombre
        self.numero = numero

    def notificar(self, mensaje):
        print("Hola soy " + self.nombre + ", y recibi el mensaje: " + mensaje)


# 5
class PetStore:
    def __init__(self, nombre, mascotas, clientes):
        self.nombre = nombre
        self.mascotas = mascotas
        self.clientes = clientes

    def es_cliente(self, cliente):
        es_cliente = False
        for xcliente in self.clientes:
            if xcliente.nombre == cliente.nombre and xcliente.numero == cliente.numero:
                es_cliente = True
        return es_cliente

    def es_mi_mascota(self, mascota):
        es_mi_mascota = False
        for xmascota in self.mascotas:
            if (
                xmascota.nombre == mascota.nombre
                and xmascota.especie == mascota.especie
                and xmascota.raza == mascota
            ):
                es_mi_mascota = True
        return es_mi_mascota

    def adopcion(self, mascota, cliente):
        if self.es_mi_mascota(mascota=mascota) and self.es_cliente(cliente=cliente):
            mascota.dueño = cliente
            filtered_list = []
            for xmascota in self.mascotas:
                if (
                    xmascota.nombre == mascota.nombre
                    and xmascota.raza == mascota.raza
                    and xmascota.especie == mascota.especie
                ):
                    continue
                else:
                    filtered_list.append(xmascota)
            self.mascotas = filtered_list
        else:
            print("No puede adoptar la mascota")


class Cliente:
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero


class Mascota:
    def __init__(self, especie, nombre, raza, dueño, color):
        self.especie = especie
        self.nombre = nombre
        self.raza = raza
        self.dueño = dueño
        self.color = color


# Number Game
# Play:
#   - Elige un numero entre 0 y 100:
#   - Tu numero es 50 ? (Yes,No)
#   > no                            | input("Tu numero es...")
#   - 50 mayor(1) o menor(-1) ?
#   > -1
#   - Tu numero es 25 ? (Yes,No)
#   > no
#   - 25 mayor(1) o menor(-1) ?
#   > 1
#   - Tu numero es 37 ? (Yes,No)
#   > Yes
#   - Excelente, me tomo 3 intentos, gane.
#   - Excelente, me tomo 21 intento, perdi.
class NumberGame:
    def __init__(self, start_number: int, end_number: int, max_tries: int) -> None:
        self.start_number = start_number
        self.end_number = end_number
        self.is_number_correct = False
        self.tries = 1
        self.max_tries = max_tries

    def play(self):
        import random

        print(
            f"Bienvenido al juego ¡Adivina el num rango {self.start_number} al {self.end_number}!"
        )

        while not self.is_number_correct:
            random_number = random.randint(self.start_number, self.end_number)
            user_answer = input(f"{random_number} es el numero pensado?(yes/no)")
            self.user_answer_is_yes(user_answer)
            if self.is_number_correct:
                self.validate_if_i_win()
            else:
                self.move_range_and_ask_again(random_number)

    def move_range_and_ask_again(self, random_number):
        self.tries += 1
        user_answer_is_lower = input("El valor que piensas es menor ? (yes/no)")
        if user_answer_is_lower.lower() == "yes":
            self.end_number = random_number
        else:
            self.start_number = random_number

    def validate_if_i_win(self):
        print("Acerte")
        if self.tries < self.max_tries:
            print(f"Gane, solo me tomo {self.tries} intentos")
        else:
            print(f"Perdi, en {self.tries} intentos")

    def user_answer_is_yes(self, user_answer):
        if user_answer.lower() == "yes":
            self.is_number_correct = True
        else:
            self.is_number_correct = False
