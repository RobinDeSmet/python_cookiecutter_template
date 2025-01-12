from pathlib import Path


def remove_docker_files():
    dockerfile_path = Path("{{cookiecutter.__project_slug}}", "Dockerfile")
    dockercompose_path = Path("{{cookiecutter.__project_slug}}", "compose.yaml")

    dockerfile_path.unlink()
    dockercompose_path.unlink()


def main():
    if "{{ cookiecutter.include_docker_files }}" != "Yes":
        remove_docker_files()

    print("Project successfuly initialized!")


if __name__ == "__main__":
    main()
