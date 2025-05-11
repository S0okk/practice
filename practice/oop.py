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


# Клиент 1: Иван
client1 = Client("Иван")
acc1 = BankAccount()
acc1.deposit(1500)
client1.add_account(acc1)

# Клиент 2: Анна
client2 = Client("Анна")
acc2 = SavingsAccount()
acc2.deposit(500)
client2.add_account(acc2)

# Покажем начальные балансы
client1.show_accounts()
client2.show_accounts()

# Перевод от Ивана к Анне
print("\nИван переводит 700 руб. Анне:")
acc1.transfer(acc2, 700)

# Балансы после перевода
print("\nПосле перевода:")
client1.show_accounts()
client2.show_accounts()