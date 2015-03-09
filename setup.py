#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
pyodesiutils
-------------
Utils library to work with DDI xml file of ODESI
"""

from os import path
from setuptools import setup

long_description = open(path.join(path.dirname(__file__), 'README.rst')).read()

setup(
    name='pyodesiutils',
    version='0.0.1alpha',
    url='https://github.com/guinslym/pyodesi_utils',
    license='MIT',
    author='Guinsly Mondesir',
    author_email='guinslym@gmail.com',
    description='Helper for ODESI xml DDI documentation file',
    long_description=long_description,
    package=['pyodesiutils'],
    classifiers=[],
        )
