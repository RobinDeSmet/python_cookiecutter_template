test:
	poetry run pytest -s -v

test-no-integration:
	poetry run pytest -s -v -m "not integration"

run:
	poetry shell & poetry run python -m {{cookiecutter.__package_slug}}