import generic
from typing import List

X86_64_LOW_RANGE = (0x00_00_00_00_00_00_00_00, 0x00_00_7F_FF_FF_FF_FF_FF)
X86_64_HIGH_RANGE = (0xFF_FF_80_00_00_00_00_00, 0xFF_FF_FF_FF_FF_FF_FF_FF)
X86_64_BYTES_LEN = 8


def generate(*args, **kwargs):
    return generic.generate(
        *args,
        **kwargs,
        pattern_length=X86_64_BYTES_LEN,
        address_ranges=[X86_64_LOW_RANGE, X86_64_HIGH_RANGE],
        reverse=True,
    )

def get_offset(pattern: List[int], value: int):
    value_tuple = generic.bytes_split_int(number=value, n=X86_64_BYTES_LEN)
    return generic.get_offset(pattern=pattern, value=value_tuple)
