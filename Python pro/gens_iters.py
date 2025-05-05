nums = [1, 2, 3]
it = iter(nums)
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3

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

for num in CountDown(3):
    print(num)  # 3, 2, 1


def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(3):
    print(num)

def even_numbers(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i ** 2
            i = i ** 2

for even in even_numbers(10):
    print(even)