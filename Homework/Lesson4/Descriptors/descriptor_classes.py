from Descriptors import TrafficSignal
from Descriptors import ProcessingAge
from Descriptors import ExpirationDate


class TrafficLight:
    signal = TrafficSignal()

    def __init__(self):
        self.signal = "RED"
        self.status = "Working"

    def change_signal(self, new_color):
        self.signal = new_color


class Person:
    age = ProcessingAge()

    def __init__(self, age):
        self.age = age


class Product:
    date = ExpirationDate()

    def __init__(self, date):
        self.date = date


def main():
    pass


if __name__ == '__main__':
    main()
