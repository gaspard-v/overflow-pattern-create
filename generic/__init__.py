from .utils import bytes_split_int
import random


def generate(length: int, pattern_length: int, address_ranges: list, allow_null_char: bool = False, reverse: bool = False) -> set:
    pattern_return = set()
    for i in range(length):
        (low, high) = random.choice(address_ranges)
        random_number = random.randrange(low, high)
        pattern_return.add(
            bytes_split_int(number=random_number,
                            n=pattern_length, reverse=reverse, allow_null_char=allow_null_char)
        )
    return pattern_return
