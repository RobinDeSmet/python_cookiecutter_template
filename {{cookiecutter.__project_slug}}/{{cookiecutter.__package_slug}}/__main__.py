import logging

from dotenv import load_dotenv

logger = logging.getLogger(__name__)

load_dotenv()
# Define global variables here that map to the env vars
# Example:
# EXAMPLE_ENV_VAR = os.getenv("EXAMPLE_ENV_VAR", "")


def main():
    logger.info("Executing {{cookiecutter.package_name}}...")

    # Do stuff

    logger.info("{{cookiecutter.package_name}} executed successfully.")


if __name__ == "__main__":
    main()
