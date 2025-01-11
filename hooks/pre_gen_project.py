import re
import sys

NAMING_CONVENTION_REGEX = r"^(?!\d)(?!.*__)(?!.*\.\.)[a-zA-Z_][a-zA-Z0-9_]*\.?(py)?$"

# Validate the project slug and package slug
if re.match("{{cookiecutter.__project_slug}}", NAMING_CONVENTION_REGEX):
    print(
        "The project name does not fit the naming conventions. Please do not use special characters or numbers."
    )
    sys.exit(1)

if re.match("{{cookiecutter.__package_slug}}", NAMING_CONVENTION_REGEX):
    print(
        "The package name does not fit the naming conventions. Please do not use special characters or numbers."
    )
    sys.exit(1)
