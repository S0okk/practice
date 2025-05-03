def factorial(n: int) -> str:
    num = 1
    for x in range(1,n+1):
        num = num * x
    return print(f'Factorial of {n} is {num}')
factorial(6)

def is_palindrom(s: str) -> bool:
    palindrom = []
    for x in s:
        palindrom.append(x)
    if palindrom == list(reversed(palindrom)):
        return print(f'{s} is palindrom')
    else:
        return print(f'{s} is not palindrom')
is_palindrom('1333331')

def find_maximum(lst: list) -> int:
    return print(f'The maximum in {lst} is {sorted(lst)[-1]}')
find_maximum([126342,2636363,34774,47430766,23346476,7423,843,136,485327])

def sum_to_n(n: int) -> str:
    first_n = n
    summary = 0
    while n>0:
        summary += n
        n-=1
    return print(f'Summary from 1 to {first_n} is {summary}')
sum_to_n(3)