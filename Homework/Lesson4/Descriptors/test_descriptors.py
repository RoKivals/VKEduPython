from Descriptors import TrafficSignal
from Descriptors import ProcessingAge


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


def main():
    p = Person(5)
    print(p.age)

if __name__ == '__main__':
    main()
