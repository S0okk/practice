from collections import namedtuple, Counter, defaultdict

# namedtuple
Point = namedtuple('Point', ['z', 'y'])
p = Point(5, 2)
print(p.z, p.y)

# Counter
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
counter = Counter(words)
print(counter)

# defaultdict
d = defaultdict(int)
d['a'] += 1
print(d)

from enum import Enum

class Status(Enum):
    NEW = 1
    IN_PROGRESS = 2
    DONE = 3

print(Status.NEW)

from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float

p = Product('Apple', 1.99)
print(p)

from typing import List, Dict

def process_data(data: List[Dict[str, str]]) -> None:
    for item in data:
        print(item)
