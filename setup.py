#!/usr/bin/env python

import setuptools
import os

setuptools.setup(
    name='geopandas-emeralds',
    version='0.0.1',
    description='Collection of utils for geopandas',
    long_description="""Collection of utils for geopandas""",
    long_description_content_type="text/markdown",
    author='Egil Moeller',
    author_email='em@emeraldgeo.no',
    url='https://github.com/emerald-geomodelling/geopandas-emeralds',
    packages=setuptools.find_packages(),
    install_requires=[
        "cython_bbox",
        "pandas",
        "scipy"
    ],
)
