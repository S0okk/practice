import unittest

# Твоя функция (замени на свою)
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Недостаточно средств')

    def get_balance(self):
        return self.__balance

    def transfer(self, other_account, amount):
        if self.__balance >= amount:
            self.withdraw(amount)
            other_account.deposit(amount)
        else:
            print("Недостаточно средств для перевода")


class SavingsAccount(BankAccount):
    def apply_interest(self, rate):
        interest = self.get_balance() * rate
        self.deposit(interest)


class Client:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account: BankAccount):
        self.accounts.append(account)

    def total_balance(self):
        return sum(acc.get_balance() for acc in self.accounts)

    def show_accounts(self):
        print(f"Счета клиента {self.name}:")
        for i, acc in enumerate(self.accounts, 1):
            print(f"  Счёт {i}: {acc.get_balance()} руб.")


# Твой тест
class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        acc = BankAccount()
        acc.deposit(1000)
        self.assertEqual(acc.get_balance(), 1000)

    def test_withdraw(self):
        acc = BankAccount()
        acc.deposit(500)
        acc.withdraw(200)
        self.assertEqual(acc.get_balance(), 300)

    def test_transfer(self):
        acc1 = BankAccount()
        acc2 = BankAccount()
        acc1.deposit(1000)
        acc1.transfer(acc2, 400)
        self.assertEqual(acc1.get_balance(), 600)
        self.assertEqual(acc2.get_balance(), 400)

    def test_overdraft_prevention(self):
        acc = BankAccount()
        acc.deposit(100)
        acc.withdraw(200)  # Должен не позволить снять
        self.assertEqual(acc.get_balance(), 100)  # Баланс не изменился

if __name__ == '__main__':
    unittest.main()
