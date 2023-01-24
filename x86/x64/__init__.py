import generic
X86_64_LOW_RANGE = (0x00_00_00_00_00_00_00_00, 0x00_00_7F_FF_FF_FF_FF_FF)
X86_64_HIGH_RANGE = (0xFF_FF_80_00_00_00_00_00, 0xFF_FF_FF_FF_FF_FF_FF_FF)


def generate(*args, **kwargs):
    print(generic.generate(100, 8, X86_64_HIGH_RANGE))
