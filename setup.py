#!/usr/bin/env python

"""Setup script for DataComparerLibrary distributions"""

import os
import re
import sys
from distutils.core import setup
from os.path import join, dirname, abspath
from pathlib import Path
from setuptools import setup

sys.path.insert(0, os.path.join('src', 'DataComparerLibrary'))

# read the contents of your README file
this_directory = Path(__file__).parent
README = (this_directory / "README.rst").read_text()

with open(join(this_directory, 'src', 'DataComparerLibrary', 'version.py')) as f:
    VERSION = re.search("\nVERSION = '(.*)'", f.read()).group(1)

def main():
    setup(name='DataComparerLibrary',
          version=VERSION,
          description="For comparing csv-files, 2d-array with a csv-file or 2d-arrays. For comparing text-files, text variable with a text-file or text variables. Including a sorting module.",
          long_description=README,
          long_description_content_type="text/x-rst",
          url="",
          author="René Philip Zuijderduijn",
          author_email="datacomparerlibrary@outlook.com",
          license="Apache",
          classifiers=[
              "License :: OSI Approved :: Apache Software License",
              "Operating System :: Microsoft :: Windows :: Windows 10",
              "Operating System :: Microsoft :: Windows :: Windows 11",
              "Programming Language :: Python :: 3.7",
              "Programming Language :: Python :: 3.8",
              "Programming Language :: Python :: 3.9",
              "Programming Language :: Python :: 3.10",
              "Programming Language :: Python :: 3.11",
              "Programming Language :: Python :: 3.12",
              "Programming Language :: Python :: 3.13",                            
          ],
          keywords='robotframework testing test-automation datacompare',
          package_dir={'': 'src'},
          packages=['DataComparerLibrary'],
          )


if __name__ == "__main__":
    main()
