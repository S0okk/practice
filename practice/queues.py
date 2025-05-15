import threading
import queue
import time
import random

# def worker(q):
#     while not q.empty():
#         item = q.get()
#         print(f"{threading.current_thread().name} обрабатывает {item}")
#         time.sleep(random.uniform(0.5, 1.5))
#         q.task_done()  # сигнал, что задача выполнена

# # Создаём очередь и наполняем её
# q = queue.Queue()
# for item in range(10):
#     q.put(item)

# # Запускаем 3 потока
# threads = []
# for _ in range(3):
#     t = threading.Thread(target=worker, args=(q,))
#     t.start()
#     threads.append(t)

# # Ждём, пока все задачи будут выполнены
# q.join()
# # print("Все задачи обработаны.")

# import threading

# counter = 0
# lock = threading.Lock()

# def increment():
#     global counter
#     for _ in range(1_000_000):
#         with lock:
#             counter += 1

# threads = []
# for _ in range(10):
#     t = threading.Thread(target=increment)
#     threads.append(t)
#     t.start()

# for t in threads:
#     t.join()

# print(f"Итоговое значение счётчика: {counter}")

# import threading

# lock = threading.RLock()

# def outer():
#     with lock:
#         print("outer acquired lock")
#         inner()

# def inner():
#     with lock:
#         print("inner acquired lock")

# thread = threading.Thread(target=outer)
# thread.start()
# thread.join()
import threading
import queue
import random

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.lock = threading.RLock()

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        return self.balance

    def transfer(self, target_account, amount):
        first, second = (self, target_account) if id(self) < id(target_account) else (target_account, self)
        with first.lock:
            with second.lock:
                if self.balance >= amount:
                    self.balance -= amount
                    target_account.deposit(amount)
        return self.balance, target_account.balance

q = queue.Queue()
for item in range(10):
    q.put(item)

acc1 = BankAccount('account_1', 10000)
acc2 = BankAccount('account_2', 10000)

def worker(q):
    while not q.empty():
        item = q.get()
        print(f"{threading.current_thread().name} обрабатывает {item}")
        acc1.transfer(acc2, random.uniform(100, 300))
        acc2.transfer(acc1, random.uniform(100, 300))
        q.task_done()

threads = []

for _ in range(10):
    t = threading.Thread(target=worker, args=(q,))
    threads.append(t)
    t.start()

q.join()

for t in threads:
    t.join()

print('All threads completed')
print(f"Баланс acc1: {acc1.balance}")
print(f"Баланс acc2: {acc2.balance}")
