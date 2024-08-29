import json


def load_json(content: str) -> dict:
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        raise RuntimeError('Data in this file is not valid.')
