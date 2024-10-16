from gendiff.src.file_handlers import collect_file_data
from gendiff.src.data_loader import load_data
from gendiff.src.diff_generator import get_diff
from gendiff.src.formatter.visualizer import visualize_tree
from gendiff.src.formatter.visualizer import DEFAULT_FORMAT


def generate_diff(filepath_1: str, filepath_2: str,
                  format: str = DEFAULT_FORMAT) -> str:
    """Accept the entered data and returns the difference in the selected format

    Args:
        filepath_1 (str): path to first file
        filepath_2 (str): path to second file
        format (str, optional): format to comparison. Default: stylish.

    Returns:
        result (str): result of visualize difference tree function
    """
    content_1 = load_data(*collect_file_data(filepath_1))
    content_2 = load_data(*collect_file_data(filepath_2))

    diff_tree = get_diff(content_1, content_2)
    return visualize_tree(diff_tree, format)
