from .utils import bytes_split_int
import random


def generate(length, pattern_length, dictionnary_range, reverse=False):
    (low, high) = dictionnary_range
    pattern_return = []
    for i in range(length):
        random_number = random.randrange(low, high)
        pattern_return.append(
            bytes_split_int(random_number, pattern_length, reverse)
        )
    return pattern_return
