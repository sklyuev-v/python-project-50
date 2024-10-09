from typing import Any
from gendiff.src.diff_generator import (
    ADDED, REMOVED, UPDATED, NESTED)


def visualize_plain(diff: list, source: str = '') -> str:
    """
    Visualize the diff to PLAIN format_

    Args:
        diff (dict): difference tree

    Returns:
        str: string in PLAIN format
    """

    result = []

    diff.sort(key=lambda node: node['key'])

    for node in diff:
        prop = f"{source}.{node['key']}" if source else node['key']

        if node['node type'] == ADDED:
            new = _normalize_data(node['value']['new'])
            result.append(f"Property '{prop}' was added with value: {new}")

        elif node['node type'] == REMOVED:
            result.append(f"Property '{prop}' was removed")

        elif node['node type'] == UPDATED:
            old = _normalize_data(node['value']['old'])
            new = _normalize_data(node['value']['new'])
            result.append(f"Property '{prop}' was updated. From {old} to {new}")

        elif node['node type'] == NESTED:
            result.append(visualize_plain(node['children'], prop))

    return '\n'.join(result)


def _normalize_data(value: Any) -> str:
    if isinstance(value, bool):
        return str(value).lower()

    elif value is None:
        return 'null'

    elif isinstance(value, int):
        return str(value)

    elif isinstance(value, dict):
        return '[complex value]'

    else:
        return f"'{value}'"
