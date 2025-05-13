import multiprocessing
import time

def worker(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")

if __name__ == "__main__":
    processes = []
    for i in range(5):
        process = multiprocessing.Process(target=worker, args=(f'Process-{i}',))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    print("All processes completed")


import time
import random

def worker(number):
    print(f"Поток {number} запущен")
    time.sleep(random.randint(1, 3))
    print(f"Поток {number} завершён")

threads = []

# TODO: Создай и запусти 5 потоков

# TODO: Жди завершения всех потоков
