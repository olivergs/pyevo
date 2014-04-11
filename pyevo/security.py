# -*- coding: utf-8 -*-
"""
PyEVO security related tools
===============================================

.. module:: pyevo.security
    :platform: Unix, Windows
    :synopsis: PyEVO security related tools
.. moduleauthor:: (C) 2013 Oliver Gutiérrez
"""

# PyEVO imports
from pyevo.strings import check_mixed_caps, check_mixed_digits, check_symbols

def password_strength(password,min_length=6,ideal_length=8):
    """
    Calculates a password strength
    
    :param password: Password to be checked
    :type password: String
    :param min_length: Minimum length for passwords. If a password is less than min_length charaters long it scores 0
    :type min_length: Integer
    :param ideal_length: Ideal length for passwords. If a password reach ideal_length or more charaters long it scores +1
    :type ideal_length: Integer
    :returns: Password strength from 0 to 5
    :rtype: Integer
    
    Examples:
    
        Less than min length
    
        >>> password_strength('abcd') # Less than min_length
        0
    
        Ideal length but no mixed elements
    
        >>> password_strength('abcdefg') # Ideal length but not 
        1
    
        Mixed caps
    
        >>> password_strength('ABCDefgh')
        2
    
        Mixed digits
    
        >>> password_strength('abcd1234')
        2
    
        Symbols
    
        >>> password_strength('ab#cdefg')
        2
    
        Full strength password
    
        >>> password_strength('AbC72&ok')
        5
        
    """
    score=0
    l=len(password)
    # Only check passwords with a minimum length
    if l >= min_length:
        # Set score to 1
        score=1
        # Medium length password
        if l >= ideal_length:
            score+=1
        # Use of mixed caps
        if check_mixed_caps(password):
            score+=1
        # Use of digits mixed with letters
        if check_mixed_digits(password):
            score+=1
        # Use of symbols
        if check_symbols(password):
            score+=1
    # Return final score
    return score