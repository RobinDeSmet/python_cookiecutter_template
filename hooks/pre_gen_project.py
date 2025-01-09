def transform_input(context):
    package_name = context["cookiecutter"]["package_name"]
    project_name = context["cookiecutter"]["project_name"]

    # Transform the names: convert to lowercase and replace spaces with hyphens
    transformed_package_name = package_name.lower().replace(" ", "-")
    transformed_project_name = project_name.lower().replace(" ", "-")

    # Update the context with the transformed package name
    context["cookiecutter"]["package_name"] = transformed_package_name
    context["cookiecutter"]["project_name"] = transformed_project_name


def main(context):
    transform_input(context)
