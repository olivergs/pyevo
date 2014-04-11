# -*- coding: utf-8 -*-
"""
PyEVO parsers module
===============================================

.. module:: pyevo.strings.parsers
    :platform: Unix, Windows
    :synopsis: PyEVO parsers module
.. moduleauthor:: (C) 2013 Oliver Gutiérrez
"""

# Python imports
import re

def key_value_parser(path,keys,separator=' '):
    """
    Key value parser for URL paths

    Uses a dictionary of keyname: callback to setup allowed parameters
    The callback will be executed to transform given value

    Examples:
    
        >>> list(sorted(key_value_parser('/invalidkey1/randomvalue/key1/0/key3/5/key1/False/key2/key3/value2/', {'key1': bool,'key2': str,'key3': int}).items()))
        [('key1', True), ('key2', 'key3'), ('key3', 5)]

        >>> list(sorted(key_value_parser('/invalidkey1/randomvalue/key1/1/key3/5/key1/0/key2/key3/value2/', {'key1': bool,'key2': str,'key3': int}).items()))
        [('key1', True), ('key2', 'key3'), ('key3', 5)]
    """
    items=path.split('/')
    keylist=keys.keys()
    data={}
    skipnext=False
    for i in range(len(items)):
        if skipnext:
            # Skip next item because it is a value
            skipnext=False
        else:
            # Get current item
            item=items[i]
            if item in keylist:
                # Next item is the value
                if i < len(items)-1:
                    try:
                        if keys[item] == bool:
                            try:
                                value=bool(int(items[i+1]))
                            except:
                                value=False
                        else:
                            value=keys[item](items[i+1])
                        data[item]=value
                        # Set flag to skip next item
                        skipnext=True
                    except:
                        pass
    return data

def extract_hashtags(text,extra=[]):
    """
    Returns a list of hashtags for given text
    """
    # Compile regular expression
    hr=re.compile(r'\#\w+')
    hashtags=hr.findall(text)
    if extra:
        # Split text in words
        words=text.split()
        # Get explicit hashtags
        for word in words:
            if word in extra:
                hashtags.append(word)
    return list(set(hashtags))

if __name__ == "__main__":
    import doctest
    doctest.testmod()