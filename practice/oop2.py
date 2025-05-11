from dataclasses import dataclass

@dataclass
class Car:
    brand: str
    year: int

    def drive(self):
        print(f"{self.brand} едет")

car1 = Car("Toyota", 2020)
car1.drive()

class Bank:
    _balance: int = 1000
    __pin: str = "1234"

    def get_balance(self):
        return self._balance
bank = Bank()
print(bank.get_balance())

class Animal:
    def speak(self):
        print("Голос")

class Dog(Animal):
    def speak(self):
        print("Гав")

dog = Dog()
dog.speak()

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Transport):
    def move(self):
        print("Еду по дороге")

class Plane(Transport):
    def move(self):
        print("Лечу в небе")
p = Plane()
c = Car()
c.move()
p.move()

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

c = Circle(4)
print(c.area())

r = Rectangle(5, 10)
print(r.area())

