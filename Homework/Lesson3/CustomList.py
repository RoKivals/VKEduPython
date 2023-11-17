from itertools import zip_longest


class CustomList(list):
    def __init__(self, *args):
        super().__init__(args)

    def __add__(self, other):
        res = CustomList()
        for x, y in zip_longest(self, other, fillvalue=0):
            res.append(x + y)

        return res

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        res = CustomList()
        for x, y in zip_longest(self, other, fillvalue=0):
            res.append(x - y)

        return res

    def __rsub__(self, other):
        return self - other


def main():
    arr = CustomList(4, 5, 6)
    print([2, 0] - arr)


if __name__ == '__main__':
    main()
