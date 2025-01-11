import pytest

@pytest.fixture(scope="function")
def setup_{{cookiecutter._package_slug}}():
    """Fixture to set up the test env."""
    pass