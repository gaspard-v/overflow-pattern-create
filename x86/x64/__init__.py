import generic

X86_64_LOW_RANGE = (0x0000_0000_0000_0000, 0x0000_7FFF_FFFF_FFFF)
X86_64_HIGH_RANGE = (0xFFFF_8000_0000_0000, 0xFFFF_FFFF_FFFF_FFFF)


def generate(*args, **kwargs):
    return generic.generate(100, 8, [X86_64_LOW_RANGE, X86_64_HIGH_RANGE])
