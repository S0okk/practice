def safe_divide(a: int, b: int) -> float:
    try:
        res=a/b
    except ZeroDivisionError:
        res = "Деление на ноль невозможно"
    return res
print(safe_divide(2,0))

def to_int(s: str) -> int:
    try:
        s = int(s)
    except ValueError:
        s = "Невозможно преобразовать в число"
    return s
print(to_int('wrh'))