# -*- coding: utf-8 -*-
"""
Facebook API tool functions
===============================================

.. module:: 
    :platform: Unix, Windows
    :synopsis: Facebook API tool functions
.. moduleauthor:: (C) 2013 Oliver Gutiérrez
"""
import urllib

def sharer_url_builder(url,title=None,summary=None,images=[]):
    """
    Builds a Facebook sharer URL from given information
    """
    data="http://www.facebook.com/sharer.php?s=100"
    data+=u"&p[url]=%s" % urllib.quote_plus(url.encode('utf-8'))
    if title is not None:
        data+=u"&p[title]=%s" % urllib.quote_plus(title.encode('utf-8'))
    if summary is not None:
        data+="&p[summary]=%s" % urllib.quote_plus(summary.encode('utf-8'))
    for image in images:
        data+="&p[images][%(index)s]=%(image)s" % { "index": images.index(image), "image": urllib.quote_plus(image.encode('utf-8'))}
    return data