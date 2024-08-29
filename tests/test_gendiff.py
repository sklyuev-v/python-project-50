from gendiff.src.gendiff import generate_diff

FLAT_JSON_1 = 'tests/fixtures/requests/file1.json'
FLAT_JSON_2 = 'tests/fixtures/requests/file2.json'
FLAT_YAML_1 = 'tests/fixtures/requests/file1.yaml'
FLAT_YAML_2 = 'tests/fixtures/requests/file2.yaml'
FLAT_YML_1 = 'tests/fixtures/requests/file1.yml'
FLAT_YML_2 = 'tests/fixtures/requests/file2.yml'

RESPONSE_STYLISH_FLAT = 'tests/fixtures/responses/stylish_flat.txt'

def test_flat_gendiff():
    with open(RESPONSE_STYLISH_FLAT, 'r') as response:
        expected_result = response.read()
    assert expected_result == generate_diff(FLAT_JSON_1, FLAT_JSON_2)


def test_yaml_flat_gendiff():
    with open(RESPONSE_STYLISH_FLAT, 'r') as response:
        excepted_result = response.read()
    assert excepted_result == generate_diff(FLAT_YAML_1, FLAT_YAML_2)


def test_yml_flat_gendiff():
    with open(RESPONSE_STYLISH_FLAT, 'r') as response:
        excepted_result = response.read()
    assert excepted_result == generate_diff(FLAT_YML_1, FLAT_YML_2)