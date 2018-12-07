# -*- coding: utf-8 -*-
"""
PyEVO HTTP utilities module
===============================================

.. module:: pyevo.http
    :platform: Windows, Linux
    :synopsis: PyEVO HTTP utilities module
.. moduleauthor:: (C) 2013 Oliver Gutiérrez
"""

# Python imports
import urllib, urllib2, json as jsonmodule

def nvp_request(url,data={},method="GET",json=False,charset='utf-8',*args,**kwargs):
    """
    Name-Value Pair request helper
    """
    if charset is not None:
        encoded_dict={}
        for k, v in data.items():
            if hasattr(v, 'encode'):
                value=v.encode(charset)
            else:
                value=v
            encoded_dict[k]=value
    encodeddata=urllib.urlencode(encoded_dict)
    if method.upper() == "POST":
        resp=urllib2.urlopen(url, encodeddata, *args, **kwargs).read()
    else:
        resp=urllib2.urlopen(url + "?" + encodeddata, *args, **kwargs).read()
    if json:
        return jsonmodule.loads(resp)
    return resp

