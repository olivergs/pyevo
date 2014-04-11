# -*- coding: utf-8 -*-
"""
PyEVO utility functions
===============================================

.. module:: pyevo.utils
    :platform: Unix, Windows
    :synopsis: PyEVO utility functions
.. moduleauthor:: (C) 2012 Oliver Gutiérrez
"""

def path_import(path):
    """
    Import a module or object from a string path

    :param path: Python path to module/object
    :type symbols: String
    :returns: A python module
    :rtype: String
    :raises: ImportError
    """
    parts = path.split('.')
    module = ".".join(parts[:-1])
    try:
        m = __import__(module)
        for comp in parts[1:]:
            m = getattr(m, comp)            
        return m
    except Exception,e:
        raise ImportError('Error importing %s module or object: %s' % (path,e))
