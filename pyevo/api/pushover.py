# -*- coding: utf-8 -*-
"""
Pushover push messaging service for mobile
===============================================

.. module:: pyevo.api.pushover
    :platform: Unix, Windows
    :synopsis: Pushover push messaging service for mobile
.. moduleauthor:: (C) 2013 Oliver Gutiérrez

TODO: Implement complete API in a class

API Specs
https://pushover.net/api

API Example
curl -s \
  -F "token=abc123" \
  -F "user=user123" \
  -F "message=hello world" \
  https://api.pushover.net/1/messages.json
"""

# PyEVO imports
from pyevo.http import nvp_request

PUSHOVER_ENDPOINT='https://api.pushover.net/1/messages.json'

def send_notification(token,user,message,endpoint=PUSHOVER_ENDPOINT,sound='pushover',**kwargs):
    """
    Sends a notification
    """
    data={
        'token': token,
        'user': user,
        'message': message,
        'sound': sound,
    }
    data.update(kwargs)
    resp=nvp_request(endpoint,data,method='POST',json=True)
    return resp