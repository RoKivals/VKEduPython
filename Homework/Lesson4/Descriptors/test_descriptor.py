import unittest
from Homework.Lesson4.Descriptors.descriptor_classes import TrafficLight, Person, Product
import datetime


class TestTrafficLight(unittest.TestCase):
    def setUp(self):
        self.tl = TrafficLight()

    def test_get(self):
        self.assertEqual(self.tl.signal, "RED")

    def test_set(self):
        self.tl.change_signal("YELLOW")

        self.assertEqual(self.tl.signal, "YELLOW")

    def test_del(self):
        del TrafficLight.signal


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.p = Person(15)
        self.p2 = Person(25)

    def test_get(self):
        self.assertEqual(self.p.age, "Несовершеннолетний")
        self.assertEqual(self.p2.age, "Совершеннолетний")

    def test_set(self):
        self.p.age = 25
        self.assertEqual(self.p.age, "Совершеннолетний")

    def test_set_errors(self):
        self.assertRaises(ValueError, self.p2.change_age, -5)
        self.assertRaises(TypeError, self.p2.change_age, [-50, 10])


class TestExpirationDate(unittest.TestCase):
    def setUp(self):
        self.product = Product(datetime.date(2024, 10, 5))

    def test_get(self):
        self.assertEqual(self.product.date, "Продукт пригоден к употреблению")

    def test_set(self):
        self.product.change_date(datetime.date(2029, 10, 5))
        self.assertEqual(self.product.date, "Продукт пригоден к употреблению")

    def test_set_errors(self):
        self.assertRaises(ValueError, self.product.change_date, datetime.date(2012, 10, 5))
        self.assertRaises(TypeError, self.product.change_date, "2014-11-11")
