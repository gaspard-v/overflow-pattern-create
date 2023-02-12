from typing import IO, Any, Tuple, Set, List


def find_offset(mylist, pattern):
    pattern = set(pattern)
    for idx, x in enumerate(mylist):
        if x in pattern:
            return idx


def get_bytes_in_int(n: int):
    if not n:
        return 1
    elif n < 0:
        raise Exception("'n' can't be negative !")
    i = 0
    while n:
        n = n >> 8
        i += 1
    return i


def bytes_split_int(
    number: int, n: int, banned_bytes: List[int] = [], reverse: bool = False
) -> Tuple:
    bytes_return = ()
    r = range(n)
    if reverse:
        r = range(n - 1, -1, -1)
    for i in r:
        b = (number >> (8 * i)) & 0xFF
        while b in banned_bytes:
            return ()
        bytes_return += (b,)
    return bytes_return


def write_to_file(file_stream: IO[Any], data: Set[Tuple]):
    for element in data:
        file_stream.write(bytes(element))


def get_offset(pattern: list[int], value: list[int]):
    find_offset(pattern, value)
