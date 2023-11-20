import time
from collections import deque


def mean(last_calls: int):
    def print_deque(calls):
        print(" ".join(str(elem) for elem in calls))

    def _mean(func):
        calls = deque()

        def wrapper(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            end = time.time()
            work_time = end - start

            print_deque(calls)
            if len(calls) == last_calls:
                calls.pop()
            calls.appendleft(work_time)
            return res

        return wrapper

    return _mean
