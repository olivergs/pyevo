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

PUSHOVER_SOUNDS=['pushover','bike','bugle','cashregister',
                  'classical','cosmic','falling','gamelan',
                  'incoming','intermission','magic','mechanical',
                  'pianobar','siren','spacealarm','tugboat',
                  'alien','climb','persistent','echo','updown','none']

def send_notification(token,user,message,endpoint=PUSHOVER_ENDPOINT,sound='pushover',**kwargs):
    """
    Sends a notification
    """
    if sound not in PUSHOVER_SOUNDS:
        raise ValueError('You must select a valid sound')

    data={
        'token': token,
        'user': user,
        'message': message,
        'sound': sound,
    }
    data.update(kwargs)
    resp=nvp_request(endpoint,data,method='POST',json=True)
    return resp