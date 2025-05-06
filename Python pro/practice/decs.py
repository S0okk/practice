def decorator(func):
    def wrapper():
        print("Перед вызовом")
        func()
        print("После вызова")
    return wrapper

@decorator
def say_hello():
    print("Привет!")

say_hello()


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

greet("Анна")
