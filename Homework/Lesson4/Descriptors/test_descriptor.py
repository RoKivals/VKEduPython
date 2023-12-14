import unittest
from Homework.Lesson4.Descriptors.descriptor_classes import TrafficLight, Person, Product


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
        pass
