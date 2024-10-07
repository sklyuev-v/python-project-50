import json
import yaml


JSON_FILE = '.json'
YAML_FILE = ('.yml', '.yaml')
WRONG_TYPE = 'Extension "{}" is not supported. Use JSON or YAML format.'
INVALID_FILE_ERROR = 'Data in this file is not valid'


def load_data(data: str, data_format: str):
    """
    Loads data from content by file extension
    Args:
        content (str): data from file as a string
        data_format (str): file extension as a string

    Raises:
        ValueError: unsupported file extension
        RuntimeError: incorrect data from file

    Returns:
        data (dict): data from file converted in dict object
    """
    if data_format == JSON_FILE:
        return load_json(data)
    elif data_format in YAML_FILE:
        return load_yaml(data)
    else:
        raise ValueError(WRONG_TYPE.format(data_format))


def load_json(content: str) -> dict:
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        raise RuntimeError(INVALID_FILE_ERROR)


def load_yaml(content: str) -> dict:
    try:
        return yaml.load(content, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        raise RuntimeError(INVALID_FILE_ERROR)
