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
