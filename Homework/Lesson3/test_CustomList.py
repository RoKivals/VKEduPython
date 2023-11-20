from CustomList import *
import unittest
from collections import namedtuple


class TestCustomList(unittest.TestCase):
    def setUp(self):
        self.test_lists = namedtuple("test_lists", ["name", "arr"])
        self.arr = CustomList(0, 5, -4, 9)

    def test_add(self):
        self.answers = [CustomList(1, 7, -9, 12),
                        CustomList(-2, 5, -1, 9)]
        lists = [self.test_lists("Summ equal length", [1, 2, -5, 3]),
                 self.test_lists("Summ different length", [-2, 0, 3])]

        for test, answer in zip(lists, self.answers):
            with self.subTest(msg=test.name):
                self.assertEqual(test.arr + self.arr, answer)

    def test_subtraction(self):
        self.answers = [CustomList(1, 5, 1, 6),
                        CustomList(0, 0, -1, 9)]

        lists = [self.test_lists("Substract equal length", [-1, 0, -5, 3]),
                 self.test_lists("Substract different length", [0, 5, -3])]

        for test, answer in zip(lists, self.answers):
            with self.subTest(msg=test.name):
                self.assertEqual(test.arr - self.arr, answer)

    def test_str(self):
        self.answers = ["-1 0 -5 3 -3",
                        "No elements in list"]

        lists = [self.test_lists("Str of filled list", CustomList(-1, 0, -5, 3)),
                 self.test_lists("Str of empty list", CustomList())]

        for test, answer in zip(lists, self.answers):
            with self.subTest(msg=test.name):
                self.assertEqual(test.arr.__str__(), answer)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
