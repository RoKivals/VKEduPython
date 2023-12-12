from Descriptors import TrafficSignal
from Descriptors import ProcessingAge
from Descriptors import ExpirationDate


class TrafficLight:
    signal = TrafficSignal()

    def __init__(self, signal="RED"):
        self.signal = signal
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
    p1 = Product(5)
    p2 = Product(6)
    p2 = Product(9)


if __name__ == '__main__':
    main()
