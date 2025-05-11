def decorator(func):
    def wrapper():
        print("Перед вызовом")
        func()
        print("После вызова")
    return wrapper

@decorator
def say_hello():
    print("Привет!")

# say_hello()


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Запуск...")
        result = func(*args, **kwargs)
        print("Завершено.")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Привет, {name}!")

# greet("Анна")

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения: {end - start:.4f} сек.")
        return result
    return wrapper

@timer
def long_task():
    time.sleep(1)
    print("Задача завершена")

# long_task()

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def greet(name):
    print(f"Привет, {name}")

# greet("Аня")

def no_negative(func):
    def wrapper(*args, **kwargs):
        if any(num < 0 for num in args):
            print("Отрицательные значения запрещены")
        else:
            return func(*args, **kwargs)
    return wrapper

@no_negative
def multiply(x, y):
    print(x * y)

# multiply(3, 4)   # 12  
# multiply(3, -4)  # Ошибка: отрицательные значения запрещены
from time import *
def timer(func):
    def wrapper(*args, **kwargs):
        cur_time = perf_counter()
        func(*args, **kwargs)
        print(f"Время выполнения: {perf_counter() - cur_time}")
    return wrapper

@timer
def slow_add():
    import time
    time.sleep(2)
    return 42
# slow_add()
# Время выполнения: 2.00 сек.

def repeat(amount):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(amount):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def beep():
    print("Бип!")

# beep()
# Бип!
# Бип!
# Бип!

def cache(func):
    saved = {}
    def wrapper(n):
        if n not in saved:
            saved[n] = func(n)
        return saved[n]
    return wrapper
@cache
def square(x):
    print(f"Вычисление квадрата для {x}")
    return x * x

print(square(4))  # Вычисление...
print(square(4))  # Повторное вычисление не должно происходить