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


def bytes_split_int(number: int, n: int, allow_null_char: bool = False, reverse: bool = False):
    bytes_return = []
    r = range(n)
    if reverse:
        r = range(n-1, -1, -1)
    for i in r:
        b = (number >> (8*i)) & 0xFF
        if not b and not allow_null_char:
            b += 1
        bytes_return.append(b)
    return bytes_return
