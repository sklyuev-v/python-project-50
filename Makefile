generate-diff:
	poetry run gendiff ./tests/fixtures/file1.json ./tests/fixtures/file2.json

lint:
	poetry run flake8 gendiff