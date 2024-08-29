def get_diff(data1: dict, data2: dict) -> dict:
    
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    diff = []

    for key in all_keys:
        if key in data1 and key not in data2:
            diff.append(add_node(key, 'removed', oldValue=data1[key]))
        elif key not in data1 and key in data2:
            diff.append(add_node(key, 'added', value=data2[key]))
        elif data1[key] == data2[key]:
            diff.append(add_node(key, 'unchanged', oldValue=data1[key]))
        else:
            diff.append(add_node(key, 'updated', value=data2[key], oldValue=data1[key]))
    return diff


def add_node(key, node_type, value=None, oldValue=None):
    node = {
        'key': key,
        'value': {
            'old': oldValue,
            'new': value
        },
        'node_type': node_type
    }

    return node

