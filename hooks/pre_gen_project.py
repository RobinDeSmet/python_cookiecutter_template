def transform_input(context):
    package_name = context["cookiecutter"]["package_name"]
    transformed_name = package_name.lower().replace(" ", "-")
    context["cookiecutter"]["package_name"] = transformed_name


def main():
    transform_input(context)
