from dataclasses import dataclass
@dataclass
class Person():
    name: str
    age: int
person_1 = Person("John", 17)
print(person_1)

def summary(*args, **kwargs):
    lst = [int(value) for value in kwargs.values()]
    return sum(args) + sum(lst)
print(summary(1, 2, 3, x=4, y=5))


from collections import Counter
collections = ['John', 'Mike', 'John', 'John', 'Alice', 'Mike', 'Larry', 'Larry']
print(Counter(collections))