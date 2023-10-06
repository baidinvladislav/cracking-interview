# {“a”: 1, “b”: 2} -> {1: “a”, 2: “b”}

# # {“a”: [1, 2], “b”: 2} -> {1: “a”, 2: “b”}


def solution(my_dict: dict) -> dict:
    result_dict = {}

    for key, val in my_dict.items():
        try:
            result_dict[val] = key
        except TypeError:
            continue

    return result_dict


hash(...) -> 'a'
hash(...) -> 'a'

{'k': [1, 2]}


class A:
    def __hash__(self):
        return 1


class B:
    def __hash__(self):
        return 1


a = A()
b = B()

d = {a: 3, b: 4}
d[a]


# [1,2,3] -> 1,2,3,1,2,3,1...


def solution(sequence: list):
    counter = 0
    while True:
        element = sequence[counter]
        yield element
        counter += 1

        if counter == len(sequence):
            counter = 0


@timeit(logger)
def f(s):
    print(s)
    time.sleep(s) 


from functools import wraps

def timeit(logger):
    @wraps
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now()
            result = func(*args, **kwargs)
            result_time = datetime.datetime.now() - start_time
            logger.info(result_time, func.__name__)
            return result

        return wrapper

    return decorator


class Device():
    def __init__(self, ip: str):
        self.ip = ip
        self.session = None

    def connect(self):
        self.session = {'1.1.1.1': 'TEST DATA',
                        '1.1.1.2': 'PROD DATA'}
        if self.ip not in self.session:
            raise ConnectionError

    def disconnect(self):
        if self.session:
            self.session = None

    def load_data(self) -> str:
        if self.session:
            return self.session[self.ip]

    def __enter__(self):
        self.connect()

    def __exit__(self):  # exc_type, exc, traceback
        self.disconnect()


try:
    device = Device(ip="0.0.0.0")
except:
    ...
finally:
    ...


with Device(ip="0.0.0.0") as device:
    print(device.load_data())

    ...  # OSError

def context_manager():
    try:
        device = Device(ip="0.0.0.0")
    except:
        ...
    finally:
        ...

import asyncio
import random

q = []  # [1]

async def consumer(queue):
    while True:
        message = queue.pop()
        print(100 / message)
        await asyncio.sleep(1)

async def producer(queue):
    while True:
        message = random.randint(1, 20)
        queue.append(message)
        await asyncio.sleep(0.5)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    loop.create_task(producer(queue=q))
    loop.create_task(consumer(queue=q))

    loop.run_forever()
