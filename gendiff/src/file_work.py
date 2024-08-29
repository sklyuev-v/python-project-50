from os import path


def read_from_file(file_path: str) -> str:
    try:
        with open(file_path, 'r') as content:
            return content.read()
    except OSError:
        raise RuntimeError(f"Failed to open file '{file_path}'")
