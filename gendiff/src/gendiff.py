import json


def get_difference(set_one, set_two):
    pass


def generate_diff(file_one, file_two):
    json_one = json.load(open(file_one))
    json_two = json.load(open(file_two))

    set_one = set(json_one)
    set_two = set(json_two)

    in_one = set_one - set_two
    in_two = set_two - set_one
    in_both = sorted(set_one | set_two)

    result_diff = []

    for item in in_both:
        if item in in_one:
            result_diff.append(f"- {item}: {json_one[item]}")
        elif item in in_two:
            result_diff.append(f"+ {item}: {json_two[item]}")
        else:
            if json_one[item] != json_two[item]:
                result_diff.append(f"- {item}: {json_one[item]}")
                result_diff.append(f"+ {item}: {json_two[item]}")
            else:
                result_diff.append(f"  {item}: {json_one[item]}")

    difference_string = '\n'.join(result_diff)
    print(difference_string)

    return difference_string
