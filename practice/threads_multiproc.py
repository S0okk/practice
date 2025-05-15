import multiprocessing
import time

def worker(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")

# if __name__ == "__main__":
#     processes = []
#     for i in range(5):
#         process = multiprocessing.Process(target=worker, args=(f'Process-{i}',))
#         processes.append(process)
#         process.start()

#     for process in processes:
#         process.join()
#     print("All processes completed")


import time
import random
import threading

# def worker(number):
#     print(f"Поток {number} запущен")
#     time.sleep(random.randint(1, 3))
#     print(f"Поток {number} завершён")

# threads = []

# for num_thread in range(5):
#     thread = threading.Thread(target=worker, args=(num_thread + 1, ))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()
#     print('All threads completed')

# def worker(number):
#     print(f"{threading.current_thread().name} started with number {number}")

# t = threading.Thread(target=worker, name="ImportantThread", args=(1,))
# print(t.name)  # ImportantThread
# t.start()


# t = threading.Thread(target=worker, args=(1,), daemon=True)


# class MyWorker(threading.Thread):
#     def __init__(self, number):
#         super().__init__()
#         self.number = number

#     def run(self):
#         print(f"Поток {self.number} запущен")
#         time.sleep(random.randint(1, 3))
#         print(f"Поток {self.number} завершён")

# # Использование
# t1 = MyWorker(1)
# t1.start()
# t1.join()

t = threading.Thread(target=worker, args=(1,))
t.start()
print(t.is_alive())  # True, если поток ещё работает
t.join()
print(t.is_alive())