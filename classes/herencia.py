from typing import List


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def greeting(self) -> str:
        return f"Hola, mi nombre es {self.name} y tengo {self.age} años."


# mirna = Person("Mirna", 26)
# print(mirna.greeting())


## --------------------------------------------------------------
class RunnerPerson(Person):
    def __init__(self, name: str, age: int, speed: float) -> None:
        Person.__init__(self, name=name, age=age)
        self.speed = speed

    def run(self) -> str:
        return f"Soy {self.name} y estoy corriendo a {self.speed} km/h"

    def greeting(self) -> str:
        return f"Hola, mi nombre es {self.name} y tengo {self.age} años. Y estoy corriendo a {self.speed} km/h"


class WalkerPerson(Person):
    def __init__(self, name: str, age: int, speed: float) -> None:
        Person.__init__(self, name, age)
        self.speed = speed

    def walk(self) -> str:
        return f"Soy {self.name} y estoy caminando a {self.speed} km/h"

    def greeting(self) -> str:
        if self.speed > 10:
            return f"{super().greeting()} y estoy caminando a {self.speed} km/h"
        return super().greeting()


mirna_corredora = RunnerPerson("Mirna Corsredora", 26, 10)
# print(mirna_corredora.run())
# print(mirna_corredora.greeting())

mirna_caminadora = WalkerPerson("Mirna Caminadora", 26, 19)
# print(mirna_caminadora.walk())
# print(mirna_caminadora.greeting())

## ---------------------------------------------------------------

## Herencia multiple
## Ojo, que exista no quiere decir que lo uses.


## Recomendaciones:
### 1. De necesitarla, que sea por las acciones no caracteristas.
### 2. Que no haya conflicto de metodos, de haber conflicto, es obligatorio resolver
### 3. Cuando se use clases abstractas o interfaces.
class RunnerWalkerPerson(RunnerPerson, WalkerPerson):
    def __init__(self, name: str, age: int, speed: float) -> None:
        RunnerPerson.__init__(self, f"{name} corredor", age, speed)
        WalkerPerson.__init__(self, f"{name} caminador", age, speed)


mirna_caminadora_corredora = RunnerWalkerPerson("Mirna", 26, 9)
# print(mirna_caminadora_corredora.run())
# print(mirna_caminadora_corredora.walk())
# print(mirna_caminadora_corredora.greeting())


## Ojo no hacer esto
class UserWithAddress:
    def __init__(self, country: str, city: str, address: str) -> None:
        self.address = address
        self.city = city
        self.country = country


class UserWithPhone:
    def __init__(self, phone: str) -> None:
        self.phone = phone


class UserWithEmail:
    def __init__(self, email: str) -> None:
        self.email = email


class User(UserWithAddress, UserWithPhone, UserWithEmail):
    def __init__(
        self, address: str, phone: str, email: str, country: str, city: str
    ) -> None:
        UserWithAddress.__init__(self, country, city, address)
        UserWithPhone.__init__(self, phone)
        UserWithEmail.__init__(self, email)


## Esto si


class Greeting:
    def greeting(self) -> str:
        raise NotImplementedError("implement")


class Walker:
    def walk(self) -> str:
        raise NotImplementedError("implement")


class Runner:
    def run(self) -> str:
        raise NotImplementedError("implement")


class PersonFull(Greeting, Runner, Walker):
    def __init__(self, name: str, age: int, speed: float) -> None:
        self.name = name
        self.age = age
        self.speed = speed

    def greeting(self) -> str:
        return f"Hola, mi nombre es {self.name} y tengo {self.age} años."

    def walk(self) -> str:
        return f"{self.greeting()} y estoy caminando a {self.speed} km/h"

    def run(self) -> str:
        return f"{self.greeting()} y estoy corriendo a {self.speed} km/h"


person_full = PersonFull("Mirna", 26, 10)
# print(person_full.greeting())
# print(person_full.walk())
# print(person_full.run())

## ------------------------------------------
## Classes abstractas o interfaces
## Ejemplo Notificador


class Notifier:
    def notify(self, mensage: str) -> None:
        raise NotImplementedError("implement")


class WhatsappGroup(Notifier):
    def notify(self, mensage: str) -> None:
        print("Desde Whatsapp")
        print(mensage)


class TelegramGroup(Notifier):
    def notify(self, mensage: str) -> None:
        print("Desde Telegram")
        print(mensage)


class SmsNotification(Notifier):
    def notify(self, mensage: str) -> None:
        print("Desde Sms")
        print(mensage)


class EmailNotification(Notifier):
    def notify(self, mensage: str) -> None:
        print("Desde Email")
        print(mensage)


class CallNotification(Notifier):
    def notify(self, mensage: str) -> None:
        print("Desde Call")
        print(mensage)


grupoFamiliar = WhatsappGroup()
grupoAmistades = WhatsappGroup()
grupoVentas = TelegramGroup()
movistar_sms = SmsNotification()
gmail = EmailNotification()
movistar_call = CallNotification()

phone_notification: List[Notifier] = [
    grupoFamiliar,
    grupoAmistades,
    grupoVentas,
    movistar_sms,
    gmail,
    movistar_call,
]
for notification in phone_notification:
    notification.notify("Hola, soy un mensaje")
