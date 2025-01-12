test:
	poetry run pytest -s -v

test-no-integration:
	poetry run pytest -s -v -m "not integration"

run:
	poetry shell & poetry run python -m {{cookiecutter.__package_slug}}

{%- if cookiecutter.include_docker_files == "Yes" -%}

up:
	docker compose up -d

build:
	docker compose up -d --build

down:
	docker compose down -v
{% endif %}