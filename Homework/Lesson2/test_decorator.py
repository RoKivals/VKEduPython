from decorator_func import mean
import random


@mean(10)
def long_func():
    cnt_digits = random.randint(200, 1000)
    digits = range(1e6, 1e10)
    arr = [random.choice(digits) for _ in range(cnt_digits)]
    return arr.sort()


def main():
    for i in range(30):
        long_func()


if __name__ == '__main__':
    main()
