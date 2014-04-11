# -*- coding: utf-8 -*-
"""

===============================================

.. module:: pyevo.api.gammu
    :platform: Unix, Windows
    :synopsis: 
.. moduleauthor:: (C) 2014 Oliver Gutiérrez
"""

# Gammu imports
import gammu
from gammu import smsd as gammusmsd

def sms_send(phone,msg,smsc=1):
    """
    Send a message using gammu
    
    Warning: This function is thread locking
    
    Returns: Gammu SMS identifier or None if sending had fail
    """
    sm = gammu.StateMachine()
    sm.ReadConfig()
    sm.Init()
    message = {
        'Text': msg,
        'SMSC': {'Location': smsc},
        'Number': phone,
    }
    return sm.SendSMS(message)

def smsd_send(phone,msg,configfile='/etc/gammu-smsdrc',smsc=1):
    """
    Send a message using gammu SMS daemon
    """
    smsd = gammusmsd.SMSD(configfile)
    message = {
        'Text': msg, 
        'SMSC': {'Location': smsc},
        'Number': phone
    }
    return smsd.InjectSMS([message])
