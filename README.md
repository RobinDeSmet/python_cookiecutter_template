## Python cookiecutter template

Personal cookiecutter for python projects.

## Usage

Install `cookiecutter` and generate a project:

```
$ pip install cookiecutter
$ cookiecutter gh:RobinDeSmet/python_cookiecutter_template -f
```

Cookiecutter will ask you for some basic info (your name, project name, python package name, etc.) and generate a base Python project for you.
Once created, run the code formatter to updates files based on your chosen names:

```
$ cd <github_repo>
```

Finally, commit all files generated by this template in a Github repository you created.
```
$ git init
$ git remote add <repository_name> <url>
$ git add .
$ git commit -m "init commit"
$ git push <repository_name>
```