from pathlib import Path


# Hook is run within the root directory of the project
def remove_docker_files():
    dockerfile_path = Path("Dockerfile")
    dockercompose_path = Path("compose.yaml")

    dockerfile_path.unlink()
    dockercompose_path.unlink()


def main():
    if "{{ cookiecutter.include_docker_files }}" != "Yes":
        remove_docker_files()

    print("Project successfuly initialized!")


if __name__ == "__main__":
    main()
