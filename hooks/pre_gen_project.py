def transform_input(context):
    package_name = context["cookiecutter"]["package_name"]
    transformed_name = package_name.lower().replace(" ", "-")
    context["cookiecutter"]["package_name"] = transformed_name


if __name__ == "__main__":
    import os
    import json

    context_file = os.path.join(os.getcwd(), ".cookiecutter.context.json")
    with open(context_file, "r") as f:
        context = json.load(f)
    transform_input(context)
    with open(context_file, "w") as f:
        json.dump(context, f)
