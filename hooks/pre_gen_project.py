import re
import sys

NAMING_CONVENTION_REGEX = r"^[a-z_][a-z0-9_]*$"


if __name__ == "__main__":
    print("Validating the variables...")

    # Validate the project slug and package slug
    if not bool(re.match("{{cookiecutter.__project_slug}}", NAMING_CONVENTION_REGEX)):
        print(
            "The project name does not fit the naming conventions. Please do not use special characters or numbers."
        )
        sys.exit(1)

    if not bool(re.match("{{cookiecutter.__package_slug}}", NAMING_CONVENTION_REGEX)):
        print(
            "The package name does not fit the naming conventions. Please do not use special characters or numbers."
        )
        sys.exit(1)

    print("All variables ok! Proceeding to project creation...")
