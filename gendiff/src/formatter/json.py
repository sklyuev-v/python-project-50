import json

from gendiff.src.diff_generator import (
    ADDED, REMOVED, UPDATED, UNCHANGED, NESTED
)


def visualize_json(diff: list) -> str:
    """
    Visualize the diff to JSON format

    Args:
        diff (list): difference tree

    Returns:
        str: string in JSON format
    """

    visualize_data = json.dumps(_visualize_nodes(diff), indent=4)
    return visualize_data


def _visualize_nodes(diff: list) -> dict:
    result = {}

    diff.sort(key=lambda node: node['key'])

    for node in diff:
        if node['node type'] == ADDED:
            result[node['key']] = {
                'value': node['value']['new']
            }

        elif node['node type'] in (REMOVED, UNCHANGED):
            result[node['key']] = {
                'value': node['value']['old']
            }

        elif node['node type'] == UPDATED:
            result[node['key']] = {
                'value': {
                    'old': node['value']['old'],
                    'new': node['value']['new']
                }
            }

        elif node['node type'] == NESTED:
            result[node['key']] = {
                'value': _visualize_nodes(node['children'])
            }

        result[node['key']]['node type'] = node['node type'].upper()

    return result
