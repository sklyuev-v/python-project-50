from typing import Any, Optional


ADDED = 'added'
REMOVED = 'removed'
UPDATED = 'updated'
UNCHANGED = 'unchanged'
NESTED = 'nested'


def get_diff(data1: dict, data2: dict) -> dict:
    """Accept two dictionary and return their difference tree

    Args:
        data1 (dict): data from first file as a python dictionary
        data2 (dict): data from second file as a python dictionary

    Returns:
        dict: difference tree of the first file (data1) and second file (data2)
    """
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    diff = []

    for key in all_keys:
        if key in data1 and key not in data2:
            diff.append(add_node(key, REMOVED, oldValue=data1[key]))

        elif key not in data1 and key in data2:
            diff.append(add_node(key, ADDED, value=data2[key]))

        elif data1[key] == data2[key]:
            diff.append(add_node(key, UNCHANGED, oldValue=data1[key]))

        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            child = get_diff(data1[key], data2[key])
            diff.append(add_node(key, NESTED, children=child))

        else:
            diff.append(
                add_node(key, UPDATED, value=data2[key], oldValue=data1[key])
            )
    return diff


def add_node(key: Any, node_type: str,
             value: Any = None, oldValue: Any = None,
             children: Optional[list] = None) -> dict:

    node = {
        'key': key,
        'value': {
            'old': oldValue,
            'new': value
        },
        'node_type': node_type
    }

    if children is not None:
        node['children'] = children

    return node
