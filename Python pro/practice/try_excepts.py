def safe_divide(a: int, b: int) -> str:
    try:
        res = a/b
    except ZeroDivisionError:
        print('Деление на 0 нельзя')
    except TypeError:
        print('a или b не числа')
    else:
        print(str(res))
    finally:
        print('Конец программы')

# Попроси пользователя ввести целое число. Если пользователь ввёл что-то другое — 
# снова попроси ввод, пока не получишь корректное значение.
def CheckingInteger () -> str:
    try:
        number = int(input('Введите integer: '))
        if type(number) is int:
            return print('Все хорошо')
    except ValueError:
        print('Некоректное значение')

# Создай класс исключения TooYoungError, если возраст пользователя < 18.

# Функция check_age(age) должна:

# принимать возраст;

# если возраст < 18, выбрасывать исключение;

# иначе — возвращать "Доступ разрешён".
class TooYoungError(Exception):
    pass

def check_age(age: int) -> str:
    if age < 18:
        raise TooYoungError('Вам нет 18 лет')
    else:
        return "Доступ разрешён"
# Задача 4: Счётчик попыток
# Напиши функцию login(), которая:

# спрашивает имя пользователя (input),

# если имя не "admin", выбрасывает ValueError,

# разрешает 3 попытки ввода, после чего выбрасывает исключение TooManyAttemptsError.

# Создай пользовательское исключение TooManyAttemptsError
class TooManyAttemptsError(Exception):
    pass

class InvalidUserError(Exception):
    pass

def login():
    attempts = 0
    while attempts < 3:
        try:
            user = input('Введите имя пользователя: ')
            if user != 'admin':
                raise InvalidUserError('Неправильное имя пользователя')
            print('Все хорошо')
            break
        except InvalidUserError as e:
            print(e)
            attempts += 1
        if attempts == 3:
            raise TooManyAttemptsError('Слишком много попыток')

# try:
#     login()
# except TooManyAttemptsError as e:
#     print(e)


# Создай функцию set_password(), которая:

# Принимает строку-пароль.

# Если длина пароля < 8 символов, выбрасывает исключение WeakPasswordError.

# Если пароль не содержит хотя бы одну цифру, выбрасывает исключение NoDigitError.

# Если всё ок — возвращает "Пароль установлен"

class WeakPasswordError(Exception):
    pass

class NoDigitError(Exception):
    pass

def set_password():
    try:
        counter = 0
        password = input()
        for letter in password:
            if letter in '0123456789':
                counter += 1
        if counter < 1:
            raise NoDigitError('Нет чисел в пароле')
        if len(password) < 8:
            raise WeakPasswordError('Пароль слабый')
    except NoDigitError as e:
        print(e)
    except WeakPasswordError as e2:
        print(e2)
    else:
        print('Пароль установлен')

# set_password()

# Задача 2: Работа с файлом
# Напиши функцию read_file(filepath), которая:

# Пытается открыть файл и прочитать его содержимое.

# Если файл не найден — выводит "Файл не найден".

# Если нет прав на чтение — выводит "Нет доступа к файлу".

# В любом случае выводит "Операция завершена".
def read_file(filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Файл не найден")
    except PermissionError:
        print("Нет доступа к файлу")
    finally:
        print("Операция завершена")

class InvalidPriceError(Exception):
    pass

class OutOfStockError(Exception):
    pass

class Product():
    def __init__(self,name: str, price: int, stock: int):
        if price < 0:
            raise InvalidPriceError('Цена не может быть отрицательной')
        self.name = name
        self.price = price
        self.stock = stock
    def buy(self, amount):
        if amount > self.stock:
            raise OutOfStockError('Не допустимое количество товара')
        self.stock -= amount
        return f"Куплено {amount} шт. товара {self.name}"
