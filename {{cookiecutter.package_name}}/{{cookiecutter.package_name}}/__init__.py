"""{{ cookiecutter.package_name }} - {{ cookiecutter.package_description }}"""

__version__ = '{{ cookiecutter.package_version }}'
__author__ = '{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>'
{%- if cookiecutter.maintainer_name %}
__maintainer__ = '{{ cookiecutter.maintainer_name }} <{{ cookiecutter.maintainer_email }}>'
{%- endif %}
__all__ = []
