from os import path
from io import open
from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file.
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.package_version }}",
    url="{{ cookiecutter.package_url }}",
    license='MIT',

    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",

    description="{{ cookiecutter.package_description }}",
    long_description=long_description,

    packages=find_packages(exclude=('tests',)),

    install_requires=[],

    zip_safe=False,

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
