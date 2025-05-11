import time
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.start_time = time.perf_counter()
        self.file = open(self.filename, 'w')
        print('Файл открыт')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        self.end_time = time.perf_counter()
        print('Файл закрыт', f'Время выполнения: {self.end_time - self.start_time:.4f} секунд')

# with ManagedFile('demo.txt') as f:
#     f.write('Hello, world!')


class Timer:
    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.perf_counter()
        print(f'Прошло времени: {self.end - self.start:.4f} секунд')

with Timer():
    print([x**2 for x in range(10**5)])
