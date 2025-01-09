# 🎉 {{cookiecutter.project_name}} 🤖

{{cookiecutter.description}}

## Environment Variables

The following environment variables need to be configured for the application to function properly:

| Variable Name              | Description                                                                                 | Default Value                                       |
|----------------------------|---------------------------------------------------------------------------------------------|--------------------------------------------------|
| `EXAMPLE_ENV_VAR`                | Description of the env var.                                                      | `The default value of the env var.`                                 |


## Maintainers

* Clone the repo and make sure you have docker and poetry installed
* Navigate to the root directory of the project
* Run `poetry install`
* Create and fill in the required details in the `.env` file. You can copy this from `.env.template`
* Run `make run`
* Run `poetry run pre-commit install` to install the pre-commit hook


## Testing
* If you want to run the test suite, run `make test`
