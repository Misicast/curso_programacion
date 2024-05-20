from unittest import TestCase

import flujos.tarea.tarea as tarea
from flujos.tarea.types import DatosDeDiccionario, Failures, Product, Punto


class TareaFirstTask(TestCase):
    def test_velocidad_must_return_50(self):
        velocidad = tarea.velocidad(punto_a=Punto(0), punto_b=Punto(50), tiempo=1)
        self.assertEqual(velocidad, 50)

    def test_velocidad_must_return_0(self):
        velocidad = tarea.velocidad(punto_a=Punto(50), punto_b=Punto(50), tiempo=1)
        self.assertEqual(velocidad, 50)

    def test_velocidad_must_return_n_50(self):
        velocidad = tarea.velocidad(punto_a=Punto(50), punto_b=Punto(0), tiempo=1)
        self.assertEqual(velocidad, 50)


class TareaSecondTask(TestCase):
    def test_model_must_match(self):
        inputData = {"name": "SomeName", "lastname": "SomeLastName", "age": 451}
        obtained = tarea.mapper(inputData)
        self.assertEqual(obtained.name, inputData["name"])
        self.assertEqual(obtained.lastname, inputData["lastname"])
        self.assertEqual(obtained.age, inputData["age"])


class TareaThirdTask(TestCase):
    def test_total_to_pay_must_include_16_percent(self):
        products = [
            Product(name="A", price=2.2),
            Product(name="A", price=1.28),
            Product(name="A", price=8.22),
            Product(name="A", price=9.54),
            Product(name="A", price=15.7),
            Product(name="A", price=74.8),
            Product(name="A", price=0.8),
            Product(name="A", price=85.5),
            Product(name="A", price=22.2),
            Product(name="A", price=825.9),
            Product(name="A", price=1.8),
        ]
        obtained = tarea.total_to_pay(products)
        self.assertEqual(obtained, sum([p.price for p in products]) * 1.16)


class TareaForthTask(TestCase):
    _products = [
        Product(name="A", price=2.2, qty_sold=1),
        Product(name="A", price=1.28, qty_sold=2),
        Product(name="A", price=8.22, qty_sold=5),
        Product(name="A", price=9.54, qty_sold=15),
        Product(name="A", price=15.7, qty_sold=15),
        Product(name="A", price=74.8, qty_sold=16),
        Product(name="A", price=0.8, qty_sold=1),
        Product(name="A", price=85.5, qty_sold=16),
        Product(name="A", price=22.2, qty_sold=16),
        Product(name="A", price=825.9, qty_sold=0),
        Product(name="A", price=1.8, qty_sold=15),
    ]

    def test_must_order_by_qty_sold(self):
        obtained = tarea.must_sold_products(self._products)
        for key, biggest_price in enumerate([16, 16, 16, 15, 15]):
            self.assertEqual(obtained[key], biggest_price)

    def test_must_len_be_5(self):
        obtained = tarea.must_sold_products(self._products)
        self.assertEqual(5, len(obtained))


class TareaFifthTask(TestCase):
    _failures = [
        Failures("electrical"),
        Failures("electrical"),
        Failures("electrical"),
        Failures("electrical"),
        Failures("electrical"),
        Failures("mechanical"),
        Failures("mechanical"),
        Failures("mechanical"),
        Failures("network"),
        Failures("network"),
        Failures("network"),
        Failures("network"),
        Failures("network"),
        Failures("network"),
        Failures("other"),
        Failures("other"),
        Failures("service"),
        Failures("service"),
    ]

    def test_must_order_by_repetition(self):
        obtained = tarea.must_repited_failures(self._failures)
        for key, qty_failures in enumerate([6, 5, 3]):
            self.assertEqual(obtained[key], qty_failures)

    def test_must_len_be_3(self):
        obtained = tarea.must_repited_failures(self._failures)
        self.assertEqual(3, len(obtained))
