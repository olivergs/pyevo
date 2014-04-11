# -*- coding: utf-8 -*-
"""
PyEVO HTML tools
===============================================

.. module:: pyevo.html
    :platform: Unix, Windows
    :synopsis: PyEVO HTML tools 
.. moduleauthor:: (C) 2012 Oliver Gutiérrez
"""

class HTMLTag(object):
    """
    HTML tag representation class
    """
    def __init__(self,element,content=None,attribs={}):
        """
        Class initialization
        """
        self.element=element
        self.content=content
        self.attribs=attribs

    def as_html(self):
        """
        Return tag as HTML
        """        
        attrs=[]
        for key,value in self.attribs.items():
            if isinstance(value,list):
                attrs.append('%s="%s"' % (key,' '.join([item.strip() for item in value])))
            else:
                attrs.append('%s="%s"' % (key,value.strip()))
        if attrs:
            tag='<%s %s>' % (self.element,' '.join(attrs))
        else:
            tag='<%s>' % self.element
        if self.content:
            return '%s%s</%s>' % (tag,self.content,self.element)
        return tag

def html_decode(s):
    """
    Returns the ASCII decoded version of the given HTML string
    """
    htmlcodes=(
        ("'", '&#39;'),
        ('"', '&quot;'),
        ('>', '&gt;'),
        ('<', '&lt;'),
        ('&', '&amp;')
    )
    for code in htmlcodes:
        s = s.replace(code[1], code[0])
    return s