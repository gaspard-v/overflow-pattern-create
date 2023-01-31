from typing import Set, Tuple
from .utils import bytes_split_int
import random


def generate(length: int, pattern_length: int, address_ranges: list, banned_bytes: list[int] = [0x0], reverse: bool = False) -> Set[Tuple[int]]:
    pattern_return = set()
    while len(pattern_return) < length:
        (low, high) = random.choice(address_ranges)
        random_number = random.randrange(low, high)
        s = bytes_split_int(number=random_number,
                            n=pattern_length, reverse=reverse, banned_bytes=banned_bytes)
        if pattern_return.issuperset({s[::-1]}):
            continue
        pattern_return.add(s)
    return pattern_return
