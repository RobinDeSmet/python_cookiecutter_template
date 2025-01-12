import re
import sys

NAMING_CONVENTION_REGEX = r"^[a-z_][a-z0-9_]*$"


if __name__ == "__main__":
    print("Validating the variables...")

    # Validate the project slug and package slug
    if not bool(re.match(NAMING_CONVENTION_REGEX, "{{cookiecutter.__project_slug}}")):
        print(
            """The package name does not fit the naming conventions.
            Please do not use special characters, other then '_', or numbers at the front of the name.
            """
        )
        sys.exit(1)

    if not bool(re.match(NAMING_CONVENTION_REGEX, "{{cookiecutter.__package_slug}}")):
        print(
            """The package name does not fit the naming conventions.
            Please do not use special characters, other then '_', or numbers at the front of the name.
            """
        )
        sys.exit(1)

    print("All variables ok! Proceeding to project creation...")
