from gendiff.src.file_work import read_from_file
from gendiff.src.data_loader import load_json
from gendiff.src.diff_generator import get_diff
from gendiff.src.formatter.stylish import stylish_render


def generate_diff(filepath_1: str, filepath_2: str) -> str:
    content_1 = load_json(read_from_file(filepath_1))
    content_2 = load_json(read_from_file(filepath_2))

    result = get_diff(content_1, content_2)
    return stylish_render(result)

    
