# -*- coding: utf-8 -*-
"""

===============================================

.. module:: 
    :platform: Unix, Windows
    :synopsis: 
    :deprecated:
.. moduleauthor:: (C) 2014 Oliver Gutiérrez
"""
from pyevo.http import nvp_request

def translate(apikey,text,from_lang,to_lang):
    """
    Translation to english function
    """
    if text:
        data={
                "key": apikey,
                "q": text,
                "source": from_lang,
                "target": to_lang,
        }
        try:
            resp=nvp_request("https://www.googleapis.com/language/translate/v2",data,json=True)
            return resp['data']['translations'][0]['translatedText']
        except:
            pass
    return None