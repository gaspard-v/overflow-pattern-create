from typing import Set, Tuple, List, Optional
from .utils import bytes_split_int, get_offset as go
import random


def generate(
    length: int,
    pattern_length: int,
    address_ranges: List[Tuple[int, int]],
    banned_bytes: List[int] = [0x0],
    reverse: bool = False,
) -> Set[Tuple]:
    pattern_return = set()
    s = ()
    nb_empty_set = 0
    while len(pattern_return) < length:
        (low, high) = random.choice(address_ranges)
        random_number = random.randrange(low, high)
        s = bytes_split_int(
            number=random_number,
            n=pattern_length,
            reverse=reverse,
            banned_bytes=banned_bytes,
        )
        if len(s) == 0:
            if nb_empty_set > 5000:
                raise Exception(
                    "more than 5000 consecutive empty sets have been generated. \
                     Check if banned bytes and address ranges are correct. \
                     This error is often due to ranges equal to banned byte. "
                )
            nb_empty_set += 1
            continue
        nb_empty_set = 0
        if pattern_return.issuperset({s[::-1]}):
            continue
        pattern_return.add(s)
    return pattern_return


def get_offset(*args, **kwargs) -> Optional[Tuple[bool, int]]:
    result = go(*args, **kwargs)
    return (result[0], result[1] // 8)
