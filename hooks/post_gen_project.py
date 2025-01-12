from pathlib import Path


def remove_docker_files():
    dockerfile_path = Path("Dockerfile")
    dockercompose_path = Path("compose.yaml")

    dockerfile_path.unlink()
    dockercompose_path.unlink()


def create_data_dir():
    data_dir_gitkeep_path = Path("data")
    data_dir_gitkeep_path.mkdir(parents=True, exist_ok=True)


def main():
    if "{{ cookiecutter.include_docker_files }}" != "Yes":
        remove_docker_files()

    create_data_dir()

    print("Project successfuly initialized!")


if __name__ == "__main__":
    main()
