# -*- coding: utf-8 -*-
"""
PyEVO reCAPTCHA API module
===============================================

.. module:: pyevo.api.recaptcha
    :platform: Unix, Windows
    :synopsis: PyEVO reCAPTCHA API module 
.. moduleauthor:: (C) 2012 Oliver Gutiérrez

TODO: Check recaptcha API module for incomplete class method get_challenge
"""

# Python imports
import urllib2, urllib

RECAPTCHA_API_SERVER='https://www.google.com/recaptcha/api'
RECAPTCHA_VERIFY_SERVER='http://www.google.com/recaptcha/api/verify'

class RECAPTCHAHelper(object):
    """
    reCAPTCHA API helper
    """
    def __init__(self,public_key,private_key,api_server=RECAPTCHA_API_SERVER,verify_server=RECAPTCHA_VERIFY_SERVER,fail_silently=True):
        """
        Class initialization
        """
        self.public_key=public_key
        self.private_key=private_key
        self.api_server=RECAPTCHA_API_SERVER
        self.verify_server=RECAPTCHA_VERIFY_SERVER
        self.fail_silently=fail_silently
        
    def verify(self,captcharesp,challenge):
        """
        Recaptcha verification
        """
        if not (captcharesp and challenge and len(captcharesp) and len(challenge)):
            return False
        # Generate request to recaptcha servers
        verifreq = urllib2.Request (
            url = self.verify_server,
            data = urllib.urlencode ({
                'privatekey': self.private_key,
                'remoteip' :  None,
                'challenge':  challenge.encode('utf-8'),
                'response' :  captcharesp.encode('utf-8'),
            }),
            headers = {
                'Content-type': 'application/x-www-form-urlencoded',
                'User-agent': 'Python'
                }
            )
        # Do request
        try:
            resp=urllib2.urlopen(verifreq)
        except:
            # In case of connection error return fail_silently as value for the verification
            return self.fail_silently
        # Check captcha response
        return_values=resp.read().splitlines();
        resp.close();
        return_code=return_values[0]
        if (return_code=='true'):
            return True
        # Failed verification
        return False
    
#    def get_challenge(self):
#        """
#        TODO: Get reCAPTCHA image and challenge data
#        """
#        challenge=
#        imgurl='http://www.google.com/recaptcha/api/image?c=%s' % challenge
#        pass