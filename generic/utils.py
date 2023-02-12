from typing import IO, Any, Tuple, Set, List, Optional


def find_offset(my_list, pattern):
    pattern = list(pattern)
    idx_pattern = 0
    for idx, element in enumerate(my_list):
        if element != pattern[idx_pattern]:
            idx_pattern = 0
            continue
        idx_pattern += 1
        if idx_pattern == len(pattern):
            return idx-7
    return -1


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


def get_offset(pattern: list[int], value) -> Optional[Tuple[bool, int]]:
    return_value = find_offset(pattern, value)
    if return_value != -1:
        return (False, return_value)
    return_value = find_offset(pattern, value[::-1])
    if return_value != -1:
        return (True, return_value)
