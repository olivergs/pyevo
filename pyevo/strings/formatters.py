# -*- coding: utf-8 -*-
"""
PyEVO string formatting tools
===============================================

.. module:: pyevo.tools.formatters
    :platform: Unix, Windows
    :synopsis: PyEVO string format tools
.. moduleauthor:: (C) 2012 Oliver Gutiérrez
"""

# Python imports
import urlparse

def currency_formatter(value,decimals=2,symbol=u'€'):
    """
    Currency formatter
    
    :param value: Currency value to be formatted
    :type value: String, float or integer
    :param decimals: Number of decimal positions
    :type decimals: Integer
    :param symbol: Currency symbol
    :type symbol: String
    :returns: Currency formatted value
    :rtype: String
    
    Examples:
    
        >>> currency(10)
        10.00€

    """
    format=u'%.DECf%s'.replace('DEC',str(decimals))
    if not value:
        value=0
    return format % (value,symbol)

def file_size_formatter(size):
    """
    File size with units formatting

    :param size: File size to be formatted
    :type size: String, float or integer
    :returns: File size with units
    :rtype: String
    
    Examples:
        >>> file_size_formatter('60')
        '60.0B'
                
        >>> file_size_formatter('600000')
        '585.94K'
        
        >>> file_size_formatter('600000000')
        '572.2M'
        
        >>> file_size_formatter('600000000000')
        '558.79G'

        >>> file_size_formatter('600000000000000')
        '545.7T'

    """
    size=float(size)
    suffixes = [('B',2**10), ('K',2**20), ('M',2**30), ('G',2**40), ('T',2**50)]
    for suffix, limit in suffixes:
        if size > limit:
            continue
        else:
            return round(size/float(limit/2**10),2).__str__()+suffix

def normalize_url(url):
    """
    Normalizes an URL

    :param url: URL to be normalized
    :type url: String
    :returns: Normalized URL in format scheme://domain/path/
    :rtype: String
    """
    # Split URL into fields
    url_fields = list(urlparse.urlsplit(url))
    if not url_fields[0]:
        # If no URL scheme assume http
        url_fields[0] = 'http'
    if not url_fields[1]:
        # If no domain path segment contains domain
        url_fields[1] = url_fields[2]
        url_fields[2] = ''
        # Rebuild URL since domain may now contain path too.
        url_fields = list(urlparse.urlsplit(urlparse.urlunsplit(url_fields)))
    if not url_fields[2]:
        # Add path portion before query params
        url_fields[2] = '/'
    return urlparse.urlunsplit(url_fields)

def phone_number_formatter(value):
    """
    Phone number formatting in groups of 3 digits from right to left

    :param value: Phone number to be formatted
    :type value: String or integer
    :returns: Phone number formatted value
    :rtype: String
    """
    newphone=''
    count=0
    for char in value[::-1]:
        newphone+=char
        count+=1
        if count % 3 == 0:
            newphone+=' '
    return newphone[::-1]

def phone_number_hide_formatter(value,number=3,symbol='X'):
    """
    Phone hiding by replacing specified number of characters by specified symbol

    :param value: Currency value to be formatted
    :type value: String, float or integer
    :param decimals: Number of decimal positions
    :type decimals: Integer
    :param symbol: Currency symbol
    :type symbol: String
    :returns: Currency formatted value
    :rtype: String
    """
    return value[:-3] + 'XXX'

def to_hashtag(value, camelcased=False, separator=''):
    """
    Convert given string to a valid hashtag

    By default the hashtag is converted to lowercase and all spaces are stripped
    """
    words=value.split(' ')
    wordlist=[]
    for word in words:
        if camelcased:
            wordlist.append(word[0].upper() + word[1:])
        else:
            wordlist.append(word)
    hashtag=u'#%s' % separator.join(wordlist)
    if not camelcased:
        return hashtag.lower()
    return hashtag
