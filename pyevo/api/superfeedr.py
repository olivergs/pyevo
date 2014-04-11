# -*- coding: utf-8 -*-
"""
Superfeeder API functions
===============================================

.. module:: 
    :platform: Unix, Windows
    :synopsis: Superfeeder API functions
.. moduleauthor:: (C) 2014 Oliver Gutiérrez
"""

# PyEVO imports
from pyevo.http import nvp_request

SUPERFEEDER_HUB_URL='http://%s.superfeedr.com'

def publish_ping(hub_name,feed_url,endpoint=SUPERFEEDER_HUB_URL):
    """
    Ping to hub to notify of refresh
    Send an POST request to http://<your-hub>.superfeedr.com, with the following params and values:
      * hub.mode="publish"
      * hub.url=<the url of the feed that was updated>
    """
    data={
        'hub.mode': 'publish',
        'hub.url': feed_url,
    }
    resp=nvp_request(endpoint % hub_name,data,method='POST')
    return resp


