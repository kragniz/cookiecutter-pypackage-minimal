{{ cookiecutter.package_name }}
{{ len(cookiecutter.package_name) * "=" }}

{% if cookiecutter.readme_pypi_badge -%}
.. image:: https://pypip.in/v/{{ cookiecutter.package_name }}/badge.png
    :target: https://pypi.python.org/pypi/{{ cookiecutter.package_name }}
    :alt: Latest PyPI version
{%- endif %}

{% if cookiecutter.readme_travis_badge and cookiecutter.readme_travis_url is not None -%}
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

{{ cookiecutter.package_name }} was written by `{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>`_.
{% if cookiecutter.maintainer_name is not None -%}
{{ cookiecutter.package_name }} was written by `{{ cookiecutter.maintainer_name }} <{{ cookiecutter.maintainer_email }}>`_.
{%- endif %}
