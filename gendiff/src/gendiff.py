from typing import Callable

from gendiff.src.file_handlers import collect_file_data
from gendiff.src.data_loader import data_loader
from gendiff.src.diff_generator import get_diff
from gendiff.src.formatter.visualizer import visualize_tree
from gendiff.src.formatter.visualizer import DEFAULT_FORMAT


def generate_diff(filepath_1: str, filepath_2: str,
                  format: str = DEFAULT_FORMAT) -> Callable[[dict], str]:
    """Accept the entered data and returns the difference in the selected format

    Args:
        filepath_1 (str): path to first file
        filepath_2 (str): path to second file
        format (str, optional): format to comparison. Default: stylish.

    Returns:
        Callable[[dict], str]:visualize difference tree
    """
    content_1 = data_loader(*collect_file_data(filepath_1))
    content_2 = data_loader(*collect_file_data(filepath_2))

    diff_tree = get_diff(content_1, content_2)
    return visualize_tree(diff_tree, format)
