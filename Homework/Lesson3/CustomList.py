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

    def is_empty(self):
        return len(self) == 0

    def sum(self):
        res = 0
        for elem in self:
            res += elem

        return res

    def __eq__(self, other):
        return self.sum() == other.sum()

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.sum() < other.sum()

    def __gt__(self, other):
        return self.sum() > other.sum()

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def __str__(self):
        if self.is_empty():
            res = "No elements in list"
        else:
            res = " ".join(str(elem) for elem in self)
            res = f"{res} {str(self.sum())}"
        return res
