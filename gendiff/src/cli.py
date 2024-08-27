import argparse


def parse_arguments():
    """
    Parses the data entered in the console to run the program.

    Parameters:
        - first_file (str): Path to first file for comparison
        - second_file (str): Path to second file for comparison
        - format (str): format for comparison

    Returns:
        args: entered values.
    """
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set the format of output')

    args = parser.parse_args()

    return args
