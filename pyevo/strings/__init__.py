# -*- coding: utf-8 -*-
"""
PyEVO string tools
===============================================

.. module:: pyevo.strings
    :platform: Unix, Windows
    :synopsis: PyEVO string tools
.. moduleauthor:: (C) 2012 Oliver Gutiérrez
"""

# Python imports
import random,string,re

def check_mixed_caps(value):
    """
    Checks if an string has mixed caps

    :param value: String to be checked
    :type value: String
    :returns: True if there are mixed caps in the string
    :rtype: Boolean
    
    Examples:    
        >>> check_mixed_caps('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse id lacus rhoncus, varius lorem vel, congue quam.'.lower())
        False
        
        >>> check_mixed_caps('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse id lacus rhoncus, varius lorem vel, congue quam.'.upper())
        False
        
        >>> check_mixed_caps('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse id lacus rhoncus, varius lorem vel, congue quam.')
        True

    """
    return re.search('[a-z]',value) is not None and re.search('[A-Z]',value) is not None

def check_mixed_digits(value):
    """
    Checks if an string has mixed digits
    
    :param value: String to be checked
    :type value: String
    :returns: True if there are mixed digits in the string
    :rtype: Boolean

    Examples:
        >>> check_mixed_digits('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse id lacus rhoncus, varius lorem vel, congue quam.')
        False
        
        >>> check_mixed_digits('123 456')
        False
        
        >>> check_mixed_digits('abcd 123 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse id lacus rhoncus, varius lorem vel, congue quam.')
        True
    
    """
    return re.search('[a-zA-Z]',value) is not None and re.search('\d+',value) is not None

def check_symbols(value):
    """
    Checks if an string has symbols
    
    :param value: String to be checked
    :type value: String
    :returns: True if there are symbols in the string
    :rtype: Boolean

    Examples:
        >>> check_symbols('Lorem ipsum')
        True
        
        >>> check_symbols('Loremipsum')
        False
        
        >>> check_symbols('123456')
        False
        
        >>> check_symbols('abcd123')
        False
        
        >>> check_symbols('ab#cd$')
        True

    """
    return re.search('[\W+]',value) is not None

def random_string(length=8,charset=string.letters+string.digits):
    """
    Generates a random string

    :param length: Random string required length
    :type length: Integer
    :param charset: String with custom choices for random string
    :type charset: String
    :returns: A random generated string
    :rtype: String
    """
    return ''.join([random.choice(charset) for i in range(length)])

def remove_chars(value,char_list=''):
    """
    Remove specific chars from a string
    
    :param value: Value to be formatted
    :type value: String
    :param char_list: String containing the characters you want to remove
    :type char_list: String
    :returns: String without punctuation symbols
    :rtype: String
    
    Example:
    
        >>> remove_chars('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse id lacus rhoncus, varius lorem vel, congue quam.', '.,:;-_/*')
        'Lorem ipsum dolor sit amet consectetur adipiscing elit Suspendisse id lacus rhoncus varius lorem vel congue quam'
    """
    return ''.join(ch for ch in value if ch not in char_list)

def char_count(text,count_spaces=False):
    """
    Counts characters in a given text

    :param text: Text for character count
    :type text: String
    :param count_spaces: Include spaces in character count 
    :type count_spaces: Boolean
    :returns: Text character count
    :rtype: Integer
    
    Examples:
        
    """
    if not count_spaces:
        text=text.replace(' ','')
    return len(text)

def word_count(text,separator=' '):
    """
    Simple word count of words split by a separator

    :param text: Text for character count
    :type text: String
    :returns: Text character count
    :rtype: Integer
    """
    return len(text.split(separator))
