import os
from ast import parse
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

name = 'pygmcluster'

# Version number set in pygmcluster/__init__.py
with open(os.path.join(name,"__init__.py")) as f:
    version = parse(next(filter(lambda line: line.startswith("__version__"), f))).body[0].value.s
description = "Python code for EM algorithm-based clustering"
long_description_content_type = "text/markdown"
url = "https://github.com/cabouman/pygmcluster"
maintainer = "Charles A. Bouman"
maintainer_email = "charles.bouman@gmail.edu"
license = "BSD-3-Clause"

packages_dir = 'pygmcluster'
packages = [packages_dir]

# Set up install for Command line interface
install_requires = ['numpy', 'matplotlib']  # external package dependencies


setup(name=name,
      version=version,
      description=description,
      long_description=long_description,
      long_description_content_type=long_description_content_type,
      url=url,
      maintainer=maintainer,
      maintainer_email=maintainer_email,
      license=license,
      packages=packages,
      install_requires=install_requires)

