#!/usr/bin/env python

from setuptools import setup

__package__ = 'mindslab-api-python-client'
__version__ = '1.0.3-beta'
__license__ = 'GPL'

install_requirements = []

setup(
    name=__package__,
    version=__version__,
    description='MindsLab API Client Library for Python',
    author='MindsLab Inc.',
    url='https://github.com/mindslab-ai/mindslab-api-python-client',
    install_requires=install_requirements,
    keywords="mindslab api client",
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5']
)
