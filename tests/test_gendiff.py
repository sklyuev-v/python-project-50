from gendiff.src.gendiff import generate_diff

FLAT_JSON_1 = 'tests/fixtures/requests/file1.json'
FLAT_JSON_2 = 'tests/fixtures/requests/file2.json'

RESPONSE_STYLISH_FLAT = 'tests/fixtures/responses/stylish_flat.txt'

def test_flat_gendiff():
    with open(RESPONSE_STYLISH_FLAT, 'r') as response:
        expected_result = response.read()
    assert expected_result == generate_diff(FLAT_JSON_1, FLAT_JSON_2)
