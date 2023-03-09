import json


def gendiff(file_one, file_two):
    json_one = json.load(open(file_one))
    json_two = json.load(open(file_two))



    set_one = set(sorted(json_one))
    set_two = set(sorted(json_two))

    in_one = set_one - set_two
    in_two = set_two - set_one
    in_both = set_one & set_two

    print(in_one)
    print(in_two)
    print(in_both)

    difference_string = ''

    return difference_string
