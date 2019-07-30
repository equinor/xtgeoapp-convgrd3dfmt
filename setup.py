#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
from glob import glob
import os
from os.path import basename
from os.path import splitext

from setuptools import setup, find_packages


def parse_requirements(filename):
    """Load requirements from a pip requirements file"""
    try:
        lineiter = (line.strip() for line in open(filename))
        return [line for line in lineiter if line and not line.startswith("#")]
    except IOError:
        return []


def src(x):
    root = os.path.dirname(__file__)
    return os.path.abspath(os.path.join(root, x))


with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = parse_requirements("requirements.txt")

setup_requirements = ["pytest-runner", "wheel", "setuptools_scm>=3.2.0"]

test_requirements = ["pytest"]

# two versions of script name
cgf1 = "convert_grid_format=" "xtgeoapp_convgrd3dfmt.cg3f:main"
cgf2 = "convgrd3dfmt=" "xtgeoapp_convgrd3dfmt.cg3f:main"


setup(
    name="xtgeoapp_convgrd3dfmt",
    # use_scm_version={
    #     "root": src(""),
    #     "write_to": src("src/xtgeoapp_convgrd3dfmt/_theversion.py"),
    # },
    description="Converting betwen 3D cornerpoint grid formats",
    long_description=readme + "\n",
    author="Equinor R&T",
    author_email="fg_gpl@equinor.com",
    url="https://github.com/equinor/convgrd3dfmt",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=[
        splitext(basename(path))[0] for path in glob("src/*.py")
    ],
    entry_points={"console_scripts": [cgf1, cgf2]},
    include_package_data=True,
    install_requires=requirements,
    tests_require=test_requirements,
    setup_requires=setup_requirements,
    zip_safe=False,
    keywords="xtgeo",
    test_suite="tests",
    license="LGPL-3.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
