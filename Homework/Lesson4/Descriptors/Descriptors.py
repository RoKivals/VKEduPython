from collections import deque
import datetime


class Descriptor:
    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"


class TrafficSignal(Descriptor):
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

        setattr(obj, self.private_name, self.colors[0])

    def __get__(self, instance, owner):
        res = getattr(instance, self.private_name)
        return res

    def __del__(self):
        if 'owner' in self.__dict__:
            self.owner.status = "Not working"

    def __str__(self):
        return f"{self.colors[0]}"


class ProcessingAge(Descriptor):

    def __set__(self, obj, new_age):
        if not isinstance(new_age, int):
            print(new_age)
            raise TypeError("Нужно число")

        if new_age < 0:
            raise ValueError("Возраст не меньше 0")
        if new_age > 120:
            raise ValueError("Столько люди не живут")

        self.age = new_age
        setattr(obj, self.private_name, self.age)

    def __get__(self, instance, owner):
        res = getattr(instance, self.private_name)
        if res >= 18:
            return "Совершеннолетний"
        return "Несовершеннолетний"


class ExpirationDate(Descriptor):

    def __set__(self, obj, new_date):
        if not isinstance(new_date, datetime.date):
            raise TypeError("Нужна дата")

        if new_date < datetime.date.today():
            raise ValueError("Данный продукт просрочен")

        setattr(obj, self.private_name, new_date)

    def __get__(self, instance, owner):
        res = getattr(instance, self.private_name)
        if res >= datetime.date.today():
            return "Продукт пригоден к употреблению"
        return "Продукт просрочен"


def main():
    pass


if __name__ == '__main__':
    main()
