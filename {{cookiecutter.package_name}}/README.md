{{ cookiecutter.package_name }}
{{ cookiecutter.package_name|count * "=" }}

{% if cookiecutter.readme_pypi_badge -%}
[![Latest PyPI version](https://img.shields.io/pypi/v/{{ cookiecutter.package_name }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.package_name }})
{%- endif %}

{% if cookiecutter.readme_travis_badge -%}
[![Latest Travis CI build status]({{ cookiecutter.readme_travis_url }}.png)]({{ cookiecutter.readme_travis_url }})
{%- endif %}

{{ cookiecutter.package_description }}

# Usage

# Installation

## Requirements

# Compatibility

# Licence

# Authors

`{{ cookiecutter.package_name }}` was written by [{{ cookiecutter.author_name }}]({{ cookiecutter.author_email }}).