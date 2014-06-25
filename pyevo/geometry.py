# -*- coding: utf-8 -*-
"""
PyEVO geometry tools
===============================================

.. module:: pyevo.geometry
    :platform: Unix, Windows
    :synopsis: PyEVO geometry tools
.. moduleauthor:: (C) 2013 Oliver Gutiérrez
"""

def maxed_rect(max_width,max_height,aspect_ratio):
    """
    Calculates maximized width and height for a rectangular area not exceding a maximum width and height.
    
    :param max_width: Maximum width for the rectangle
    :type max_width: float
    :param max_height: Maximum height for the rectangle
    :type max_height: float
    :param aspect_ratio: Aspect ratio for the maxed rectangle
    :type aspect_ratio: float
    :returns: A tuple with width and height of the maxed rectangle
    :rtype: Tuple
    
    Examples:

        >>> maxed_rect(800,600,aspect_ratio=4/3.)
        (800.0, 600.0)

        >>> maxed_rect(800,1600,aspect_ratio=800/600.)
        (800.0, 600.0)

        >>> maxed_rect(1600,600,aspect_ratio=800/600.)
        (450.0, 600.0)
    
    """
    mw=float(max_width)
    mh=float(max_height)
    ar=float(aspect_ratio)
    
    # Do by width
    w=mw
    h=(mw/(aspect_ratio))
    if h > mh:
        # Do by height
        h=mh
        w=(mh/(aspect_ratio))
    return(w,h)
