#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import x86.x64 as x64
import generic.utils as utils
import sys


def main():
    data = x64.generate(length=100)
    utils.write_to_file(sys.stdout.buffer, data)


if __name__ == "__main__":
    main()
