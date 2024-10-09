from typing import Any
from gendiff.src.diff_generator import (
    ADDED, REMOVED, UPDATED, UNCHANGED,  # NESTED
)

NESTED_INDENT = 4
SIGN_INDENT = 2


def visualize_stylish(diff: list) -> str:
    return f"{{\n{_visualize_nodes(diff)}\n}}"


def _visualize_nodes(diff: dict, lvl: int = 1) -> str:
    result = []
    indent = ' ' * (lvl * NESTED_INDENT - SIGN_INDENT)

    diff.sort(key=lambda node: node['key'])

    for node in diff:
        if node['node type'] == ADDED:
            result.append(
                _make_line(node['key'], node['value']['new'], '+', lvl)
                # f"  + {node['key']}: {str(node['value']['new']).lower()}"
            )

        elif node['node type'] == REMOVED:
            result.append(
                _make_line(node['key'], node['value']['old'], '-', lvl)
                # f"  - {node['key']}: {str(node['value']['old']).lower()}"
            )

        elif node['node type'] == UPDATED:
            result.append(
                _make_line(node['key'], node['value']['old'], '-', lvl)
                # f"  - {node['key']}: {str(node['value']['old']).lower()}"
            )
            result.append(
                _make_line(node['key'], node['value']['new'], '+', lvl)
                # f"  + {node['key']}: {str(node['value']['new']).lower()}"
            )

        elif node['node type'] == UNCHANGED:
            result.append(
                _make_line(node['key'], node['value']['old'], ' ', lvl)
                # f"    {node['key']}: {str(node['value']['old']).lower()}"
            )

        else:  # node['node type'] == NESTED:
            result.extend(
                [f"{indent}  {node['key']}: {{",
                 _visualize_nodes(node['children'], lvl=lvl + 1),
                 f"{indent}  }}"]
            )

    return '\n'.join(result)


def _normalize_data(value: Any) -> str:
    if isinstance(value, bool):
        return str(value).lower()

    elif value is None:
        return 'null'

    else:
        return str(value)


def _make_line(key: Any, value: Any, sign: str, lvl: int) -> str:
    result = []
    indent = ' ' * (lvl * NESTED_INDENT - SIGN_INDENT)
    lvl += 1

    if isinstance(value, dict):
        before_str = f"{indent}{sign} {key}: {{"
        after_str = f"{indent}  }}"
        result.extend([before_str, _format_dict(value, lvl), after_str])
    else:
        result.append(f"{indent}{sign} {key}: {_normalize_data(value)}")

    return '\n'.join(result)


def _format_dict(dict_value: dict, lvl: int) -> str:
    result = []

    for key, value in dict_value.items():
        result.append(_make_line(key, value, ' ', lvl))

    return '\n'.join(result)
