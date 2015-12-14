import setuptools

setuptools.setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.package_version }}",
    url="{{ cookiecutter.package_url }}",

    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",

    description="{{ cookiecutter.package_description }}",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
