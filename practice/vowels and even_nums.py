def get_even_numbers(start:int, end: int) -> list:
    # even_nums = []
    # for x in range(start, end+1):
    #     if x % 2 == 0:
    #         even_nums.append(x)
    # return even_nums
    return [x for x in range(range(start, end+1)) if x % 2 == 0]

def count_vowels(s:str) -> int:
    counter = 0
    for letter in s.lower():
        if letter in 'aeyuio':
            counter += 1
    return counter