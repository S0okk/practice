import threading
import time

def worker(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(f'Thread-{i}',))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads finished")

from multiprocessing import Process
import time

def worker(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")

processes = []
for i in range(5):
    p = Process(target=worker, args=(f'Process-{i}',))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

print("All processes finished")
