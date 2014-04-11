# -*- coding: utf-8 -*-
"""
PyEVO file utility functions
===============================================

.. module:: 
    :platform: Unix, Windows
    :synopsis: PyEVO file utility functions
.. moduleauthor:: (C) 2014 Oliver Gutiérrez
"""

# Python imports
import os, datetime

def last_modification_datetime(path):
    """
    Returns last modification datetime for a given path
    """
    mtime=os.path.getmtime(path)
    return datetime.datetime.fromtimestamp(mtime)

def concatenate_files(filelist,endchar=''):
    """
    Concatenates the contents of the files in a file path list
    """
    data=''
    for fpath in filelist:
        fd=open(fpath,'r')
        data+=fd.read()+endchar
        fd.close()
    return data
    