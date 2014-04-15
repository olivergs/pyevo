# -*- coding: utf-8 -*-
"""
PyEVO Python utility library setup script
===============================================

.. module:: pyevo
    :platform: Unix, Windows
    :synopsis: Python utility library setup script
.. moduleauthor:: (C) 2013 Oliver Gutiérrez
"""
# Python imports
import os
from distutils.core import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='pyevo',
    packages =['pyevo'],
    version='0.1',
    description='PyEVO Python utility library',
    long_description=README,
    license='MIT License',
    author="Oliver Gutiérrez",
    author_email="ogutsua@gmail.com",
    url = 'https://github.com/R3v1L/pyevo',
    keywords = ['pyevo', 'utility', ],
    classifiers = [],
    # download_url = '',
)