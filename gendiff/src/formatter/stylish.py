def stylish_render(data: list) -> str:
    result = []

    data.sort(key=lambda node: node['key'])

    for node in data:
        if node['node_type'] == 'removed':
            result.append(f"  - {node['key']}: {str(node['value']['old']).lower()}")
        elif node['node_type'] == 'added':
            result.append(f"  + {node['key']}: {str(node['value']['new']).lower()}")
        elif node['node_type'] == 'unchanged':
            result.append(f"    {node['key']}: {str(node['value']['old']).lower()}")
        elif node['node_type'] == 'updated':
            result.append(f"  - {node['key']}: {str(node['value']['old']).lower()}")
            result.append(f"  + {node['key']}: {str(node['value']['new']).lower()}")

    return '{\n' + '\n'.join(result) + '\n}'