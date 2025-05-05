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
        CheckingInteger()

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
check_age(18)