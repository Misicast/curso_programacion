from unittest import TestCase

import flujos.tarea.tarea as tarea
from flujos.tarea.types import (
    Email,
    Failures,
    LanguageDictionary,
    Product,
    ProductCategory,
    Punto,
)


class Part1Case1(TestCase):
    def test_velocidad_must_return_50(self):
        velocidad = tarea.velocidad(punto_a=Punto(0), punto_b=Punto(50), tiempo=1)
        self.assertEqual(velocidad, 50)

    def test_velocidad_mustj_return_0(self):
        velocidad = tarea.velocidad(punto_a=Punto(50), punto_b=Punto(50), tiempo=1)
        self.assertEqual(velocidad, 0)

    def test_velocidad_must_return_n_50(self):
        velocidad = tarea.velocidad(punto_a=Punto(50), punto_b=Punto(0), tiempo=1)
        self.assertEqual(velocidad, -50)


class Part1Case2(TestCase):
    def test_model_must_match(self):
        inputData = {"name": "SomeName", "lastname": "SomeLastName", "age": 451}
        obtained = tarea.mapper(inputData)
        self.assertEqual(obtained.name, inputData["name"])
        self.assertEqual(obtained.lastname, inputData["lastname"])
        self.assertEqual(obtained.age, inputData["age"])


class Part1Case3(TestCase):
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


class Part1Case4(TestCase):
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
        obtained = tarea.most_sold_products(self._products)
        for key, biggest_price in enumerate([16, 16, 16, 15, 15]):
            self.assertEqual(obtained[key].qty_sold, biggest_price)

    def test_must_len_beCase5(self):
        obtained = tarea.most_sold_products(self._products)
        self.assertEqual(5, len(obtained))


class Part1Case5(TestCase):
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
        obtained = tarea.most_repited_failures(self._failures)
        for key, qty_failures in enumerate(["network", "electrical", "mechanical"]):
            self.assertEqual(obtained[key].name, qty_failures)

    def test_must_len_beCase3(self):
        obtained = tarea.most_repited_failures(self._failures)
        self.assertEqual(3, len(obtained))


class Part2Case1(TestCase):
    def test_maximun_must_be_10(self):
        expected = 10
        obtained = tarea.maximun(list(range(0, expected + 1)))
        self.assertEqual(expected, obtained)

    def test_maximun_must_be_0(self):
        expected = 0
        obtained = tarea.maximun(list(range(-10, expected + 1)))
        self.assertEqual(expected, obtained)

    def test_maximun_must_be_n_10(self):
        expected = -10
        obtained = tarea.maximun(list(range(-100, expected + 1, 2)))
        self.assertEqual(expected, obtained)

    def test_maximun_must_be_300(self):
        expected = 300
        obtained = tarea.maximun(list(range(150, expected + 1, 2)))
        self.assertEqual(expected, obtained)


class Part2Case2(TestCase):
    words = [
        "The",
        "The",
        "quick",
        "brown",
        "brown",
        "brown",
        "fox",
        "jumped",
        "jumped",
        "jumped",
        "over",
        "the",
        "lazy",
        "dog",
    ]

    def test_should_count_3_the_in_words(self):
        expected = 3
        obtained = tarea.count_words(Part2Case2.words)
        self.assertEqual(expected, obtained["The"])

    def test_should_count_3_brown_in_words(self):
        expected = 3
        obtained = tarea.count_words(Part2Case2.words)
        self.assertEqual(expected, obtained["brown"])

    def test_should_count_3_jumped_in_words(self):
        expected = 3
        obtained = tarea.count_words(Part2Case2.words)
        self.assertEqual(expected, obtained["jumped"])

    def test_should_count_1_quick_fox_over_lazy_and_dog_in_words(self):
        expected = 1
        obtained = tarea.count_words(Part2Case2.words)
        self.assertEqual(expected, obtained["quick"])
        self.assertEqual(expected, obtained["fox"])
        self.assertEqual(expected, obtained["over"])
        self.assertEqual(expected, obtained["lazy"])
        self.assertEqual(expected, obtained["dog"])


class Part2Case3(TestCase):
    emails = [
        Email(
            by="me",
            to="you",
            content="random text",
            is_favorite=True,
            is_urgent=False,
            subject="Random email",
        ),
        Email(
            by="you",
            to="me",
            content="random text",
            is_favorite=False,
            is_urgent=True,
            subject="Random email",
        ),
        Email(
            by="you",
            to="me",
            content="random text",
            is_favorite=True,
            is_urgent=True,
            subject="Random email",
        ),
    ]

    def test_len_must_be_2(self):
        expected = 2
        obtained = tarea.get_favorites(Part2Case3.emails)
        self.assertEqual(expected, len(obtained))

    def test_all_of_the_obtained_must_be_favorite(self):
        expected = True
        obtained = tarea.get_favorites(Part2Case3.emails)
        for email in obtained:
            self.assertEqual(expected, email.is_favorite)


class Part2Case4(TestCase):
    categories_consumed = [
        ProductCategory(name="bisuteria", product_qty_sold=5, total_amount_sold=5),
        ProductCategory(name="carteras", product_qty_sold=3, total_amount_sold=5),
        ProductCategory(name="gorras", product_qty_sold=4, total_amount_sold=5),
        ProductCategory(name="perfume", product_qty_sold=2, total_amount_sold=5),
        ProductCategory(name="zapatos", product_qty_sold=1, total_amount_sold=5),
    ]

    def test_must_be_in_order_bisuteria_gorras_carteras_perfume_zapatos(self):
        expected = ["bisuteria", "gorras", "carteras", "perfume", "zapatos"]
        obtained = tarea.most_consumed_categories(Part2Case4.categories_consumed)
        for key, cat_expected in enumerate(expected):
            self.assertEqual(obtained[key].name, cat_expected)


class Part2Case5(TestCase):
    categories_consumed = [
        ProductCategory(name="bisuteria", product_qty_sold=5, total_amount_sold=1),
        ProductCategory(name="carteras", product_qty_sold=3, total_amount_sold=3),
        ProductCategory(name="gorras", product_qty_sold=4, total_amount_sold=2),
        ProductCategory(name="perfume", product_qty_sold=2, total_amount_sold=4),
        ProductCategory(name="zapatos", product_qty_sold=1, total_amount_sold=5),
    ]

    def test_must_be_in_order_zapatos_perfume_carteras_gorras_bisuteria(self):
        expected = [
            "zapatos",
            "perfume",
            "carteras",
            "gorras",
            "bisuteria",
        ]
        obtained = tarea.most_amount_consumed_category(Part2Case5.categories_consumed)
        for key, cat_expected in enumerate(expected):
            self.assertEqual(obtained[key].name, cat_expected)


class Part2Case6(TestCase):
    categories = [
        ProductCategory(name="bisuteria", product_qty_sold=5, total_amount_sold=1),
        ProductCategory(name="carteras", product_qty_sold=3, total_amount_sold=3),
        ProductCategory(name="gorras", product_qty_sold=4, total_amount_sold=2),
        ProductCategory(name="perfume", product_qty_sold=2, total_amount_sold=4),
        ProductCategory(name="zapatos", product_qty_sold=1, total_amount_sold=5),
        ProductCategory(name="bisuteria", product_qty_sold=5, total_amount_sold=1),
    ]

    def test_must_be_in_order_bisuteria_gorras_carteras_perfume_zapatos(self):
        total_product_sold = sum([c.product_qty_sold for c in Part2Case6.categories])
        categories_percent = (
            (category, category.product_qty_sold / total_product_sold)
            for category in Part2Case6.categories
        )
        expected: dict[str, float] = {}
        for category_percent in categories_percent:
            if category_percent[0].name in expected:
                expected[category_percent[0].name] += category_percent[1]
            else:
                expected[category_percent[0].name] = category_percent[1]
        obtained = tarea.most_consumed_categories_percent(Part2Case6.categories)
        for key, value in expected.items():
            self.assertEqual(obtained[key], value)


class Part3Case1(TestCase):
    names = [
        "Beatriz Golindano",
        "Mirna Silva",
        "Cruz Ortiz",
        "Gabriel Ortiz Golindano",
    ]

    def test_must_return_two_char_str_for_each_name(self):
        obtained = tarea.get_avatar_initials(Part3Case1.names)
        for name in obtained:
            self.assertEqual(len(name), 2)

    def test_must_match_each_name_with_its_avatar_initials(self):
        expected = ["BG", "MS", "CO", "GO"]
        obtained = tarea.get_avatar_initials(Part3Case1.names)
        for key, value in enumerate(expected):
            self.assertEqual(obtained[key], value)


class Part3Case2(TestCase):
    urls_template = [
        "www.youtube.com/{id}/details",
        "www.google.com/{id}/details",
        "www.facebook.com/{id}/details",
        "www.twitter.com/{id}/details",
        "www.instagram.com/{id}/details",
    ]

    def test_must_return_id_45(self):
        expected = "45"
        urls = (url.replace("{id}", expected) for url in Part3Case2.urls_template)
        for url in urls:
            obtained = tarea.get_id_from_url(url)
            self.assertEqual(expected, obtained)

    def test_must_return_id_SOmeText(self):
        expected = "SOmeText"
        urls = (url.replace("{id}", expected) for url in Part3Case2.urls_template)
        for url in urls:
            obtained = tarea.get_id_from_url(url)
            self.assertEqual(expected, obtained)


class Part3Case3(TestCase):
    products = [
        Product(name="A", price=20.2, qty_sold=2),
        Product(name="B", price=30.3, qty_sold=3),
        Product(name="C", price=40.4, qty_sold=4),
        Product(name="AL", price=40.4, qty_sold=4),
    ]

    def test_must_return_only_one_element_when_search_is_B(self):
        expected = 1
        obtained = tarea.search_products(Part3Case3.products, "B")
        self.assertEqual(expected, len(obtained))

    def test_must_return_only_one_element_when_search_is_C(self):
        expected = 1
        obtained = tarea.search_products(Part3Case3.products, "B")
        self.assertEqual(expected, len(obtained))

    def test_must_return_2_element_when_search_is_A(self):
        expected = 2
        obtained = tarea.search_products(Part3Case3.products, "A")
        self.assertEqual(expected, len(obtained))

    def test_must_product_name_with_search_when_is_AL(self):
        expected = "AL"
        obtained = tarea.search_products(Part3Case3.products, expected)
        self.assertEqual(expected, obtained[0].name)

    def test_must_product_name_with_search_when_is_B(self):
        expected = "B"
        obtained = tarea.search_products(Part3Case3.products, expected)
        self.assertEqual(expected, obtained[0].name)

    def test_must_product_name_with_search_when_is_C(self):
        expected = "C"
        obtained = tarea.search_products(Part3Case3.products, expected)
        self.assertEqual(expected, obtained[0].name)


class Part3Case4(TestCase):
    lang = LanguageDictionary()

    def setUp(self) -> None:
        Part3Case4.lang.add("hello", "hola").add("world", "mundo")
        return super().setUp()

    def test_must_return_lang_hola_for_hello(self):
        expected = Part3Case4.lang["hello"]
        obtained = tarea.translate(Part3Case4.lang, "hello", "Hola")
        self.assertEqual(expected, obtained)

    def test_must_return_lang_mundo_for_world(self):
        expected = Part3Case4.lang["world"]
        obtained = tarea.translate(Part3Case4.lang, "world", "Mundo")
        self.assertEqual(expected, obtained)

    def test_must_add_word_to_dictionary_and_return_default_value(self):
        expected = "defecto"
        obtained = tarea.translate(Part3Case4.lang, "default", expected)
        self.assertEqual(expected, obtained)
        self.assertEqual(Part3Case4.lang["default"], expected)


class Part3Case5(TestCase):
    def test_should_return_only_fizz(self):
        for test in range(2, 44, 6):
            obtained = tarea.fizz_buzz(test)
            self.assertEqual("fizz", obtained)

    def test_should_return_only_buzz(self):
        for test in range(5, 55, 10):
            obtained = tarea.fizz_buzz(test)
            self.assertEqual("buzz", obtained)

    def test_should_return_only_fizzbuzz(self):
        for test in range(10, 100, 10):
            obtained = tarea.fizz_buzz(test)
            self.assertEqual("fizzbuzz", obtained)
