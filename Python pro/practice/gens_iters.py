nums = [1, 2, 3]
it = iter(nums)
# print(next(it))  # 1
# print(next(it))  # 2
# print(next(it))  # 3

class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # сам является итератором

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# for num in CountDown(3):
#     print(num)  # 3, 2, 1


def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# for num in count_up_to(3):
#     print(num)

def even_numbers(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i ** 2
            i = i ** 2

# for even in even_numbers(10):
#     print(even)



class CountUpTo:
    def __init__(self, end):
        self.end = end+1
        self.current = 1

    def __iter__(self):
        return self  # сам является итератором

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value
c = CountUpTo(5)
# for num in c:
#     print(num)

def even_numbers(num: int):
    for eve in range(0,num+1):
        if eve % 2 == 0:
            yield eve
# for i in even_numbers(10):
#     print(i)

words = ["one", "two", "three"]
def add_prefix(words: list, prefix: str):
    for word in words:
        word = prefix + word
        yield word
# for item in add_prefix(words, "num_"):
#     print(item)

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
# gen = fibonacci()
# for _ in range(6):
#     print(next(gen))

def reverse_range(t: int, f: int):
    for i in range(f-1, t-1, -1):
        yield i
# for i in reverse_range(3, 7):
#     print(i)

def cycle(lst: list):
    while True:
        for word in lst:
            yield word
gen = cycle(['A', 'B', 'C'])
# for _ in range(7):
#     print(next(gen))