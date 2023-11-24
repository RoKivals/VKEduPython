from collections import deque


class TrafficSignal:
    __colors = ('RED', 'YELLOW', 'GREEN')

    def __init__(self):
        self.colors = deque(self.__colors)

    def __set__(self, obj, new_color):
        if not isinstance(new_color, str):
            raise TypeError("Нужна строка")

        if new_color.upper() not in self.__colors:
            raise ValueError("Такого цвета нет")

        self.owner = obj
        while new_color.upper() != self.colors[0]:
            self.colors.append(self.colors.popleft())

        setattr(obj, "color", self.colors[0])

    def __get__(self, instance, owner):
        res = getattr(instance, "color")
        return res

    def __del__(self):
        self.owner.status = "Not working"

    def __str__(self):
        return f"{self.colors[0]}"


class Adult:
    def __init__(self):
        self.age = None

    def __set__(self, obj, new_age):
        if new_age < 0:
            raise ValueError("Возраст не меньше 0")
        if new_age > 120:
            raise ValueError("Столько люди не живут")

        setattr(obj, "age", self.age)

    def __get__(self, instance, owner):
        res = getattr(instance, "age")
        if res >= 18:
            return "Совершеннолетний"
        return "Несовершеннолетний"


def main():
    pass


if __name__ == '__main__':
    main()
