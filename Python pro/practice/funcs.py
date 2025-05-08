square = list(map(lambda x: x ** 2, range(11)))
print(square)

words = ["apple", "is", "banana", "go", "pineapple"]
sort_words = list(filter(lambda x: len(x) > 4, words))
print(sort_words)

from functools import reduce
lst = [1, 5, 3, 64, 235, 135, 437]
suma = reduce(lambda x, y: x + y, lst)
print(suma)

names = ["Alice", "Bob"]
scores = [90, 85]
connected = list(zip(names, scores))
print(connected)

new_lst = ["data", "science", "AI"]
truth = []
for letter in new_lst:
    if len(letter) > 0:
        truth.append(True)
    else:
        truth.append(False)
print(all(truth))

nums = [1, 3, 7, 10]
any_of = []
for num in nums:
    if num % 2 == 0:
        any_of.append(True)
    else:
        any_of.append(False)
print(all(truth))

values = ["one", "two", "three"]
for i, val in enumerate(values):
    print(i, val)
