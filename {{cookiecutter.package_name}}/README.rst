{{ cookiecutter.package_name }}
{{ cookiecutter.package_name|count * "=" }}

{% if cookiecutter.readme_pypi_badge -%}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.package_name }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.package_name }}
    :alt: Latest PyPI version
{%- endif %}

{% if cookiecutter.readme_travis_badge -%}
.. image:: {{ cookiecutter.readme_travis_url }}.png
   :target: {{ cookiecutter.readme_travis_url }}
   :alt: Latest Travis CI build status
{%- endif %}

{{ cookiecutter.package_description }}

Usage
-----

Installation
------------

Requirements
^^^^^^^^^^^^

Compatibility
-------------

Licence
-------

Authors
-------

`{{ cookiecutter.package_name }}` was written by `{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>`_.
