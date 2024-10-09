from os import path


def collect_file_data(file_path: str) -> tuple:
    """
    Return content from file and file extension
    Args:
        file_path (str): path to file

    Returns:
        tuple: content from file, file extension
    """
    return _read_from_file(file_path), _get_file_extension(file_path)


def _read_from_file(file_path: str) -> str:
    try:
        with open(file_path, 'r') as content:
            return content.read()
    except OSError:
        raise RuntimeError(f"Failed to open file '{file_path}'")


def _get_file_extension(file_path: str) -> str:
    _, file_extension = path.splitext(file_path)
    return file_extension.lower()
