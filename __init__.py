#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import x86.x64 as x64
import generic.utils as utils
import sys


def main():
    data = x64.generate(length=100)
    with open("oof.txt", "wb") as data_file:
        utils.write_to_file(data_file, data)


if __name__ == "__main__":
    main()
