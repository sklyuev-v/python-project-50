# !usr/bin/env python3
from gendiff.src.cli import parse_arguments
from gendiff.src.gendiff import generate_diff


def main():
    """
    Entry point for application
    """
    args = parse_arguments()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == "__main__":
    main()
