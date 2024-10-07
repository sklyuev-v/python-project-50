from gendiff.src.gendiff import generate_diff
from gendiff.src.formatter.visualizer import FORMAT_STYLISH
from gendiff.src.formatter.visualizer import FORMAT_JSON
from gendiff.src.formatter.visualizer import FORMAT_PLAIN


FLAT_JSON_1 = 'tests/fixtures/requests/file1.json'
FLAT_JSON_2 = 'tests/fixtures/requests/file2.json'
FLAT_YAML_1 = 'tests/fixtures/requests/file1.yaml'
FLAT_YAML_2 = 'tests/fixtures/requests/file2.yaml'
FLAT_YML_1 = 'tests/fixtures/requests/file1.yml'
FLAT_YML_2 = 'tests/fixtures/requests/file2.yml'
NESTED_JSON_1 = 'tests/fixtures/requests/file3.json'
NESTED_JSON_2 = 'tests/fixtures/requests/file4.json'
NESTED_YAML_1 = 'tests/fixtures/requests/file3.yaml'
NESTED_YAML_2 = 'tests/fixtures/requests/file4.yaml'
NESTED_YML_1 = 'tests/fixtures/requests/file3.yml'
NESTED_YML_2 = 'tests/fixtures/requests/file4.yml'

RESPONSE_STYLISH_FLAT = 'tests/fixtures/responses/stylish_flat.txt'
RESPONSE_STYLISH_NESTED = 'tests/fixtures/responses/stylish_nested.txt'
RESPONSE_JSON_FLAT = 'tests/fixtures/responses/json_flat.txt'
RESPONSE_JSON_NESTED = 'tests/fixtures/responses/json_nested.txt'
RESPONSE_PLAIN_FLAT = 'tests/fixtures/responses/plain_flat.txt'
RESPONSE_PLAIN_NESTED = 'tests/fixtures/responses/plain_nested.txt'


# FLAT JSON TESTS - STYLISH, JSON, PLAIN FORMATS

def test_json_flat_gendiff_stylish():
    with open(RESPONSE_STYLISH_FLAT, 'r') as response:
        expected_result = response.read()
    assert expected_result == generate_diff(
        FLAT_JSON_1, FLAT_JSON_2, FORMAT_STYLISH)


def test_json_flat_gendiff_json():
    with open(RESPONSE_JSON_FLAT, 'r') as response:
        expected_result = response.read()
    assert expected_result == generate_diff(
        FLAT_JSON_1, FLAT_JSON_2, FORMAT_JSON)


def test_json_flat_gendiff_plain():
    with open(RESPONSE_PLAIN_FLAT, 'r') as response:
        expected_result = response.read()
    assert expected_result == generate_diff(
        FLAT_JSON_1, FLAT_JSON_2, FORMAT_PLAIN)


# NESTED JSON TESTS - STYLISH, JSON, PLAIN FORMATS

def test_json_nested_gendiff_stylish():
    with open(RESPONSE_STYLISH_NESTED, 'r') as response:
        expected_result = response.read()
    assert expected_result == generate_diff(
        NESTED_JSON_1, NESTED_JSON_2, FORMAT_STYLISH)


def test_json_nested_gendiff_json():
    with open(RESPONSE_JSON_NESTED, 'r') as response:
        expected_result = response.read()
    assert expected_result == generate_diff(
        NESTED_JSON_1, NESTED_JSON_2, FORMAT_JSON)


def test_json_nested_gendiff_plain():
    with open(RESPONSE_PLAIN_NESTED, 'r') as response:
        expected_result = response.read()
    assert expected_result == generate_diff(
        NESTED_JSON_1, NESTED_JSON_2, FORMAT_PLAIN)

# FLAT YAML TESTS - STYLISH, JSON, PLAIN FORMATS


def test_yaml_flat_gendiff_stylish():
    with open(RESPONSE_STYLISH_FLAT, 'r') as response:
        expected_result = response.read()
    assert expected_result == generate_diff(
        FLAT_YAML_1, FLAT_YAML_2, FORMAT_STYLISH)


def test_yaml_flat_gendiff_json():
    with open(RESPONSE_JSON_FLAT, 'r') as response:
        expected_result = response.read()
    assert expected_result == generate_diff(
        FLAT_YAML_1, FLAT_YAML_2, FORMAT_JSON)


def test_yaml_flat_gendiff_plain():
    with open(RESPONSE_PLAIN_FLAT, 'r') as response:
        expected_result = response.read()
    assert expected_result == generate_diff(
        FLAT_YAML_1, FLAT_YAML_2, FORMAT_PLAIN)


# NESTED YAML TESTS - STYLISH, JSON, PLAIN FORMATS

def test_yaml_nested_gendiff_stylish():
    with open(RESPONSE_STYLISH_NESTED, 'r') as response:
        expected_result = response.read()
    assert expected_result == generate_diff(
        NESTED_YAML_1, NESTED_YAML_2, FORMAT_STYLISH)


def test_yaml_nested_gendiff_json():
    with open(RESPONSE_JSON_NESTED, 'r') as response:
        expected_result = response.read()
    assert expected_result == generate_diff(
        NESTED_YAML_1, NESTED_YAML_2, FORMAT_JSON)


def test_yaml_nested_gendiff_plain():
    with open(RESPONSE_PLAIN_NESTED, 'r') as response:
        expected_result = response.read()
    assert expected_result == generate_diff(
        NESTED_YAML_1, NESTED_YAML_2, FORMAT_PLAIN)


# FLAT YML TESTS - STYLISH, JSON, PLAIN FORMATS

def test_yml_flat_gendiff_stylish():
    with open(RESPONSE_STYLISH_FLAT, 'r') as response:
        expected_result = response.read()
    assert expected_result == generate_diff(
        FLAT_YML_1, FLAT_YML_2, FORMAT_STYLISH)


def test_yml_flat_gendiff_json():
    with open(RESPONSE_JSON_FLAT, 'r') as response:
        expected_result = response.read()
    assert expected_result == generate_diff(FLAT_YML_1, FLAT_YML_2, FORMAT_JSON)


def test_yml_flat_gendiff_plain():
    with open(RESPONSE_PLAIN_FLAT, 'r') as response:
        expected_result = response.read()
    assert expected_result == generate_diff(
        FLAT_YML_1, FLAT_YML_2, FORMAT_PLAIN)


# NESTED YML TESTS - STYLISH, JSON, PLAIN FORMATS

def test_yml_nested_gendiff_stylish():
    with open(RESPONSE_STYLISH_NESTED, 'r') as response:
        expected_result = response.read()
    assert expected_result == generate_diff(
        NESTED_YML_1, NESTED_YML_2, FORMAT_STYLISH)


def test_yml_nested_gendiff_json():
    with open(RESPONSE_JSON_NESTED, 'r') as response:
        expected_result = response.read()
    assert expected_result == generate_diff(
        NESTED_YML_1, NESTED_YML_2, FORMAT_JSON)


def test_yml_nested_gendiff_plain():
    with open(RESPONSE_PLAIN_NESTED, 'r') as response:
        expected_result = response.read()
    assert expected_result == generate_diff(
        NESTED_YML_1, NESTED_YML_2, FORMAT_PLAIN)
