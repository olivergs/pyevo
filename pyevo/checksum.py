# -*- coding: utf-8 -*-
"""
PyEVO checksum utility functions
===============================================

.. module:: pyevo.checksum
    :platform: Unix, Windows
    :synopsis: Checksum utility functions
.. moduleauthor:: (C) 2013 Oliver Gutiérrez
"""

# Python imports
import string

def mod10(value):
    """
    Luhn (mod10) algorithm verification
    
    :param value: Value to be checked
    :type value: Numeric string or integer
    :returns: MOD10 checksum value
    :rtype: single digit integer value 0-9
    """
    num = map(int, str(value))
    return sum(num[::-2] + [sum(divmod(d * 2, 10)) for d in num[-2::-2]]) % 10 == 0

def spanish_dni_letter(dni):
    """
    Generates spanish DNI letter
    
    :param dni: DNI numeric part
    :type dni: Numeric string or integer
    :returns: DNI letter
    :rtype: Single letter string
    """
    letters='TRWAGMYFPDXBNJZSQVHLCKE'
    return letters[int(dni[:8])%23]

def spanish_nie_letter(nie):
    """
    Generates spanish NIE letter

    :param nie: NIE numeric part
    :type nie: Numeric string or integer
    :returns: NIE letter
    :rtype: Single letter string
    """
    letters='XYZ'
    return spanish_dni_letter(str(letters.index(nie[0]))+nie[1:])

def spanish_bank_account_control_digits(entity,office,account):
    """
    Calculate spanish bank account control digits

    :param entity: Four digit bank account entity code
    :type entity: Numeric string or integer
    :param office: Four digit bank account entity code
    :type office: Numeric string or integer
    :param account: Ten digit bank account entity code
    :type account: Numeric string or integer
    :returns: Spanish bank account control digits
    :rtype: Two digits string
    """
    entity=int(entity)
    office=int(office)
    account=int(account)
    dcs=''
    mults=(10,9,7,3,6,1,2,4,8,5)
    numbers=[
        (entity+office).zfill(10),
        account.zfill(10)
    ]
    for num in numbers:
        accum=0
        for pos in range(10):
            accum+=int(num[pos])*mults[pos]
        mod=accum%11
        if mod==10:
            dcs+='1'
        else:
            dcs+=str(mod)
    return dcs

def calculate_iban(countrycode,accountnum,printing=True):
    """
    IBAN account number calculation
    
    :param countrycode: Country code for the account
    :type countrycode: String
    :param accountnum: Account number
    :type accountnum: String
    :param printing: Return IBAN in printing format
    :type printing: True or False
    :returns: IBAN account number
    :rtype: String
    """
    countryval=''
    for digit in countrycode.upper():
        countryval+=str(string.ascii_uppercase.index(digit)+10)
    countryval+='00'
    dc=str(98-(int(accountnum+countryval)%97))
    iban=countrycode.upper()+dc+accountnum
    if printing:
        piban=''
        i=0
        j=4
        block=iban[i:j]
        while block:
            piban+=block+' '
            i+=4
            j+=4
            block=iban[i:j]
        return piban.strip()
    else:
        return iban