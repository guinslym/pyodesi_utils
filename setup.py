#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
pyodesiutils
-------------
Utils library to work with DDI xml file of ODESI
"""

from os import path
from distutils.core import setup

long_description = open(path.join(path.dirname(__file__), 'README.rst')).read()

setup(
    name='pyodesiutils',
    version='0.0.2',
    url='https://github.com/guinslym/pyodesi_utils',
    license='MIT',
    author='Guinsly Mondesir',
    install_requires=['beautifulsoup4'],
    author_email='guinslym@gmail.com',
    description='Helper for uottawa ODESI xml DDI documentation file',
    long_description=long_description,
    keywords = ['ddi', 'idd', 'statcan', 'survey', 'xml'],
    package=['pyodesiutils'],
    classifiers=[
    'Programming Language :: Python :: 2.7',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python'
    ],
        )
