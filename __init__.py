#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import x86.x64 as x64
import generic.utils as utils
import sys
import argparse

possible_


def parse_arguments():
    parser = argparse.ArgumentParser(prog="overflow-pattern-create",
                                     description="Create pattern for many architecture such as x86",
                                     epilog="overflow-pattern-create")
    parser.add_argument("--arch",
                        help="")


def main():
    data = x64.generate(length=100)
    utils.write_to_file(sys.stdout.buffer, data)


if __name__ == "__main__":
    main()
