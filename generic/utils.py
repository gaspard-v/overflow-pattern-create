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


def bytes_split_int(number: int, n: int):
    bytes_return = []
    for i in range(n):
        b = (number >> (8*i)) & 0xFF
        bytes_return.append(b)
    return bytes_return
