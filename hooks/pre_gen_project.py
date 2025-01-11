import re
import sys

NAMING_CONVENTION_REGEX = r"^(?!\d)(?!.*__)(?!.*\.\.)[a-zA-Z_][a-zA-Z0-9_]*\.?(py)?$"

# Convert characters to lower case and change spaces to underscores
"""
{{ cookiecutter.update({"project_name": cookiecutter.project_name.lower().replace(" ", "_") }) }}
{{ cookiecutter.update({"package_name": cookiecutter.package_name.lower().replace(" ", "_") }) }}
"""


if re.match("{{cookiecutter.project_name}}", NAMING_CONVENTION_REGEX):
    print(
        "The project name does not fit the naming conventions. Please do not use special characters or numbers."
    )
    sys.exit(1)

if re.match("{{cookiecutter.package_name}}", NAMING_CONVENTION_REGEX):
    print(
        "The package name does not fit the naming conventions. Please do not use special characters or numbers."
    )
    sys.exit(1)
