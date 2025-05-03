def filter_and_uppercase(lst: list) -> list:
    return list(map(lambda x: x.upper(), filter(lambda x: len(x) > 5, lst)))

print(filter_and_uppercase(['hi', 'world', 'amazing', 'python', 'future']))