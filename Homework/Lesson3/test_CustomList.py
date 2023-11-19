from CustomList import *
import unittest


class TestCustomList(unittest.TestCase):
    def setUp(self):
        self.arr = CustomList(0, 5, -4, 9)

    def test_add(self):
        sum1 = self.arr + CustomList(1, 2, -5, 3)
        sum2 = self.arr + [1, 2, -5, 3]

        sum3 = self.arr + CustomList(-2, 0, 3)
        sum4 = self.arr + [-2, 0, 3]

        sum5 = CustomList(-14, 5, 23, 19, -30) + self.arr
        sum6 = [-14, 5, 23, 19, -30] + self.arr

        sum7 = CustomList() + CustomList()

        self.assertEqual(sum1, CustomList(1, 7, -9, 12))
        self.assertEqual(sum2, CustomList(1, 7, -9, 12))

        self.assertEqual(sum3, CustomList(-2, 5, -1, 9))
        self.assertEqual(sum4, CustomList(-2, 5, -1, 9))

        self.assertEqual(sum5, CustomList(-14, 10, 19, 28, -30))
        self.assertEqual(sum6, CustomList(-14, 10, 19, 28, -30))
        self.assertEqual(sum7, CustomList())

    def test_diff(self):
        sum1 = self.arr + CustomList(1, 2, -5, 3)
        sum2 = self.arr + [1, 2, -5, 3]

        sum3 = self.arr + CustomList(-2, 0, 3)
        sum4 = self.arr + [-2, 0, 3]

        sum5 = CustomList(-14, 5, 23, 19, -30) + self.arr
        sum6 = [-14, 5, 23, 19, -30] + self.arr

        sum7 = CustomList() + CustomList()

        self.assertEqual(sum1, CustomList(1, 7, -9, 12))
        self.assertEqual(sum2, CustomList(1, 7, -9, 12))

        self.assertEqual(sum3, CustomList(-2, 5, -1, 9))
        self.assertEqual(sum4, CustomList(-2, 5, -1, 9))

        self.assertEqual(sum5, CustomList(-14, 10, 19, 28, -30))
        self.assertEqual(sum6, CustomList(-14, 10, 19, 28, -30))
        self.assertEqual(sum7, CustomList())


def main():
    pass


if __name__ == '__main__':
    main()
