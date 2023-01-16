import string
from typing import List, Tuple, Type, TypeAlias, Union

Intervales_type: TypeAlias = List[Tuple[int, int]]
Length_type: TypeAlias = int


def divide_chunks(my_list: List, n: int):
    return [my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1) // n)]


def generate(lenght: Length_type, pattern_length: Length_type, intervales: Intervales_type):
    number_intervales = len(intervales)
    sets_bounds = []
    for index_i, (low, high) in enumerate(intervales):
        offset = (high - low) // pattern_length
        low_set = low
        high_set = low+offset
        sets_bounds.append([])
        for p in range(pattern_length):
            sets_bounds[index_i].append((low_set, high_set))
            low_set = high_set
            high_set = high_set+offset
    pass
