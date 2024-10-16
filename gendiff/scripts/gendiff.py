# !usr/bin/env python3
from typing import NoReturn

from gendiff.src.cli import parse_arguments
from gendiff.src.gendiff import generate_diff


def main() -> NoReturn:
    """
    Entry point for application

    Return:
        Print result of the generate_diff function()
    """
    args = parse_arguments()
    try:
        print(generate_diff(args.first_file, args.second_file, args.format))
    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    main()
