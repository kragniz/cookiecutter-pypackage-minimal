cookiecutter-pypackage-minimal
==============================

A minimal [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) template for 
developing Machine Learning projects in Python in a Visual Studio Code 
[Dev Container](https://code.visualstudio.com/docs/devcontainers/containers). This
project was forked from a library template by [kragniz](https://github.com/kragniz/cookiecutter-pypackage-minimal)
and uses the approach described in 
[my blog](https://srinathh.medium.com/developing-in-python-with-containers-4c73e0dcb)
to create a dev container.

Usage
-----

Install Cookiecutter if needed and then use the tool to instantiate your project folder
```
pip install cookiecutter
cookiecutter gh:srinathh/cookiecutter-data-science-devcontainer
```

Then test that it builds in Docker
```
cd <your project name>
docker build --tag test .
```

Then when you open your project in Visual Studio Code, it should ask you if you want to 
to open the folder as a Dev Container which will have all dependencies as well as the package
inside the project library folder installed
```
code .
```

If you change your dependencies, press `F1` inside VS Code to pull up the Command Palette
and select "Dev Containers: Rebuild container" option.

Folder Structure
----------------

```
package_name                      - The root folder will be named as package_name in cookiecutter
|
|-- .devcontainer
|  |-- devcontainer.json           - Configuration for VS Code dev container that points to Dockerfile
|
|-- package_name                   - Folder to store the library and application code for your project.
|  |-- __init__.py                   This will be pip installed in the container.
|
|-- data                           - Folder to store data locally. All context will be .gitignored
|
|-- notebooks                      - Folder for your notebooks. you can import package_name inside
|
|-- tests                          - Folder for tests
|  |-- test_sample.py
|
|-- .gitignore
|-- Dockerfile                     - The dockerfile to create a container
|-- README.md
|-- requirements.txt               - Project dependencies go here
|-- setup.py
```