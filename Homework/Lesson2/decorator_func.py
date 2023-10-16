import time


def mean(func, last_calls: list):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        work_time = end - start
        print(f"Функция {func.__name__} работала {time} секунд")
        return res

    return wrapper


def main():
    @mean(10)
    def foo(arg1):
        pass

    @mean(2)
    def boo(arg1):
        pass

    for _ in range(100):
        foo("Walter")


if __name__ == '__main__':
    main()
