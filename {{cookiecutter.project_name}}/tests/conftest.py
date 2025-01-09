import pytest

@pytest.fixture(scope="function")
def setup_{{cookiecutter.package_name}}():
    """Fixture to set up the test env."""
    pass