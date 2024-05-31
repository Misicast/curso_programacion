from unittest import TestCase

from classes.tarea.tarea import Car, CarFactory, FibonacciGen


class PartICase1CarFactory(TestCase):
    factory = CarFactory(name="test", ubicacion="testu", marca="toyota")

    def test_must_fabricate_car(self):
        obtained = PartICase1CarFactory.factory.fabricar(
            tipo="camioneta", ac=True, ce=True, añofab="test", modelo="TestM"
        )
        self.assertTrue(obtained is Car)

    def test_must_fabricate_car_of_the_brand_toyota(self):
        obtained = PartICase1CarFactory.factory.fabricar(
            tipo="camioneta", ac=True, ce=True, añofab="test", modelo="TestM"
        )
        self.assertEqual(obtained.marca, PartICase1CarFactory.factory.marca)


class PartICase2Folder(TestCase):
    pass


class PartICase3Fibonacci(TestCase):
    def test_fibonacci_gen_must_match_sequence_1_2_3_5_8_13(self):
        sequence = [1, 2, 3, 5, 8]
        for value in sequence:
            obtained = FibonacciGen().generar()
            self.assertEqual(obtained, value)


class PartICase4TelephoneCarrierCentral(TestCase):
    pass


class PartICase5PetStore(TestCase):
    pass


class PartICase6NumberGame(TestCase):
    pass
