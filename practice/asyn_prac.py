import asyncio
import time
async def wait_and_print(text, delay):
    await asyncio.sleep(delay)
    print(text)
async def main():
    await asyncio.gather(wait_and_print("Первый", 2), wait_and_print("Второй", 1))

# asyncio.run(main())

async def print_numbers():
    await asyncio.sleep(1)
    for num in range(1, 4):
        print(num)

async def print_letters():
    await asyncio.sleep(1)
    for letter in "ABC":
        print(letter)

async def print_symbols():
    await asyncio.sleep(1)
    for symbol in "!@#":
        print(symbol)

async def main():
    await asyncio.gather(print_numbers(), print_letters(), print_symbols())
# asyncio.run(main())

def Timer(coroutine):
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = await coroutine(*args, **kwargs)
        end = time.perf_counter()
        print(f"Время выполнения: {end - start:.4f} секунд")
        return result
    return wrapper

@Timer
async def slow_func():
    await asyncio.sleep(2)

@Timer
async def faster_func():
    await asyncio.sleep(1)

async def main():
    await asyncio.gather(slow_func(), faster_func())
# asyncio.run(main())


async def download_file(filename, delay):
    await asyncio.sleep(delay)
    print(f"{filename} загружен за {delay} сек")


async def main():
    results = await asyncio.gather(
        download_file("file1.txt", 3),
        download_file("file2.txt", 2),
        download_file("file3.txt", 1)
    )
    print("Все файлы загружены:", results)

# asyncio.run(main())

sem = asyncio.Semaphore(2)

async def download(name):
    async with sem:
        print(f"Начало: {name}")
        await asyncio.sleep(2)
        print(f"Завершено: {name}")

async def main():
    await asyncio.gather (download("file1.txt"), download("file2.txt"), download("file3.txt"), download("file4.txt"), download("file5.txt"))
# asyncio.run(main())

queue = asyncio.Queue()
for i in range(5):
    queue.put_nowait(f'task-{i+1}')

async def worker(name, queue):
    while not queue.empty():
        task = await queue.get()
        print(f"{name} обрабатывает: {task}")
        await asyncio.sleep(1)
        queue.task_done()

async def main():
    await asyncio.gather(
        worker("First", queue),
        worker("Second", queue)
    )

asyncio.run(main())