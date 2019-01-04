# coding: utf-8
from __future__ import print_function

import os

LONG_DESCRIPTION_FILES = ["README.rst", "README.md", "README.txt", "README"]


def drop_extra_long_description_files():
    long_description_file = '{{ cookiecutter.long_description_file }}'
    to_drop = [name for name in LONG_DESCRIPTION_FILES if name != long_description_file]
    print("- Droping extra long description files: {0}".format(", ".join(to_drop)))
    for name in to_drop:
        os.remove(name)


if __name__ == '__main__':
    print("Running post-generate hooks...")
    drop_extra_long_description_files()
    print("Done.")
