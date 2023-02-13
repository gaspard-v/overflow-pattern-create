#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import x86.x64 as x64
import generic.utils as utils
import argparse
import sys
from ast import literal_eval

availible_architecture = ["x86_64", "x86_32"]
availible_action = ["create_pattern", "get_offset"]


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="overflow-pattern-create",
        description="Create pattern for many architecture such as x86",
        epilog="overflow-pattern-create",
    )
    parser.add_argument(
        "--arch",
        help=f"specify which architure you want to find the offset, choices are {availible_architecture}",
        choices=availible_architecture,
        type=str,
        required=True,
    )
    parser.add_argument(
        "--action",
        help=f"Specifie what the script should do, choices are {availible_action}",
        choices=availible_action,
        type=str,
        required=True
    )
    parser.add_argument(
        "--length",
        help="specify the length of the pattern, in bytes",
        type=int,
        default=100,
        required=False
    )
    parser.add_argument(
        "--file",
        help="specify which file the pattern would be read or written in",
        type=str,
        required=False
    )
    parser.add_argument(
        "--value",
        help="specify the value of your EIP/RIP register for exemple (in hexadecimal like 0x12345678)",
        type=str,
        default="-1",
        required=False
    )
    parser.add_argument(
        "--exclude",
        help="exclude bytes from the generation pattern algorithm",
        nargs="+",
        default=[],
        required=False
    )
    parser.add_argument("--version", action="version", version="%(prog)s 1.0")
    args = parser.parse_args()
    try:
        args.value = literal_eval(args.value)
    except ValueError as value_error:
        print(f"cannnot parse value \"{args.value}\"", file=sys.stderr)
        exit(2)
    try:
        args.exclude = list(map(lambda x: int(x), args.exclude))
    except:
        try:
            args.exclude = list(map(lambda x: literal_eval(x), args.exclude))
        except Exception as err:
            print(
                f"Cannot parse excluded bytes ! Error {err}", file=sys.stderr)
            exit(2)
    return args


def create_pattern(script_args):
    if script_args.arch == "x86_64":
        data = x64.generate(length=script_args.length,
                            banned_bytes=script_args.exclude)
        with open(script_args.file, "wb") as f:
            utils.write_to_file(f, data)
    return 0


def get_offset(script_args):
    pattern_int = []
    with open(script_args.file, "rb") as f:
        while byte := f.read(1):
            byte_int = int.from_bytes(byte, "big")
            pattern_int.append(byte_int)
    result = x64.get_offset(pattern_int, script_args.value)
    if not result:
        print("pattern not found")
        return 1
    (reversed, offset) = result

    print(f"offset: {offset} byte(s)")
    if reversed:
        print(f"Warning, the pattern is reversed")


def main():
    script_args = parse_arguments()
    return_code = 1
    if script_args.action == "create_pattern":
        return_code = create_pattern(script_args)
    elif script_args.action == "get_offset":
        return_code = get_offset(script_args)
    exit(return_code)


if __name__ == "__main__":
    main()
