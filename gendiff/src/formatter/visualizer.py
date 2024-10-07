from typing import Callable
from gendiff.src.formatter.stylish import visualize_stylish
from gendiff.src.formatter.json import visualize_json
from gendiff.src.formatter.plain import visualize_flat

FORMAT_STYLISH = 'stylish'
FORMAT_PLAIN = 'plain'
FORMAT_JSON = 'json'
FORMATS = (FORMAT_STYLISH, FORMAT_JSON, FORMAT_PLAIN)
DEFAULT_FORMAT = FORMAT_STYLISH


def visualize_tree(diff: dict, format: str) -> Callable[[dict], str]:
    """Calling visualize function based on selected format:
    stylish, plain or json

    Args:
        diff (dict): difference tree between two files
        format (str):format (stylish, plain or json)

    Raises:
        ValueError: unsupported visualize format

    Returns:
        Callable[[dict], str]: calling visualize function in the selected format
    """
    if format == FORMAT_STYLISH:
        return visualize_stylish(diff)
    elif format == FORMAT_PLAIN:
        return visualize_flat(diff)
    elif format == FORMAT_JSON:
        return visualize_json(diff)
    else:
        raise ValueError('''Incorrect format.
                          Use "stylish", "plain" or "json" formats.''')
