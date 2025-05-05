from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass

class CurrentAccount(Account):
    def __init__(self):
        self.__balance = 0
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if self.__balance >= amount*1.01:
            self.__balance = self.__balance - amount*1.01
        else:
            print("На счету не достаточно средств")
    def get_balance(self):
        return self.__balance


class SavingsAccount(Account):
    def __init__(self):
        self.__balance = 0
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
        else:
            print("На счету не достаточно средств")
    def get_balance(self):
        return self.__balance
    def apply_interest(self, rate):
        interest = self.__balance * rate
        return self.deposit(interest)
