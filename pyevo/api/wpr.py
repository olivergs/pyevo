# -*- coding: utf-8 -*-
"""
PyEVO World Premium Rates WPR Premium SMS services API
===============================================
.. module:: pyevo.api.wpr
    :platform: Unix, Windows
    :synopsis: PyEVO reCAPTCHA API module 
.. moduleauthor:: (C) 2012 Oliver Gutiérrez

TODO: Implement rest of methods

# API Example

Request:
    URL: http://medios.micropagos.net/gencode/servlet/GCCommands?command=<COMMAND>&login=<USER>&passwd=<PASSWORD>&code=<CODE>&serv=<SERVID>&used=<ACTION> 

    <COMMAND> = check | mark | gettime check --> Se empleará para verificar que el código es válido. mark --> Se emplea para marcar el código como usado, de tal manera que no pueda usarse de nuevo. gettime --> Se emplea para solicitar la fecha y hora en la que nuestro sistema asignó el código. 
    <USER> --> Nombre clave del cliente que será asignado por WPR para un ALIAS y servicio concreto 
    <PASSWORD> --> Clave asignada para el cliente por WPR para un ALIAS y servicio concreto 
    <CODE> --> Código que se quiere verificar. WPR se lo habrá dado al usuario tras el envío de mensajes correspondientes. 
    <SERVID> --> Identificador de servicio que será asignado para el cliente por WPR para un ALIAS 
    <ACTION> --> 0 | 1 (Sólo será útil para el caso de COMANDO=check) 0 --> No hará nada 1 --> Si el código es válido, además lo marcará como "Usado" con lo que no se podrá volver a utilizar. De esta manera, en una única consulta el cliente puede verificar el código y marcarlo como usado. 

Response: 
    check: 
        CLOSED --> Indica que el código ha sido asignado, es decir, que es válido. 
        ERROR --> Si el código no se ha encontrado. 
        NOTUSER --> Si los datos proporcionados de identificación USUARIO, CLAVE y/o SERVID no son correctos. 

    mark: 
        ERROR --> Si el código no se ha encontrado. 
        NOTUSER --> Si los datos proporcionados de identificación 
        USUARIO, CLAVE y/o SERVID no son correctos.
        OK --> Indica que el código se ha marcado como usado 
        KO --> Indica que el código no se ha podido marcar como usado. 

    gettime: 
        CLOSED|YYYY-MM-DD|HH:MM:SS --> Si el código es válido, nos devuelve la fecha(YYYY-MM-DD) y la hora (HH:MM:SS) 
        RROR --> Si el código no es válido. 
        NOTUSER --> Si los datos proporcionados de identificación USUARIO, CLAVE y/o SERVID no son correctos.
"""

# PyEVO imports
from pyevo.http import nvp_request

# Variables
WPR_ENDPOINT='http://medios.micropagos.net/gencode/servlet/GCCommands'

def gencode_check(code,username,password,servid,mark=False,endpoint=WPR_ENDPOINT):
    """
    Checks if a code is valid and marks it as used if specified
    """
    data={
        'command': 'check',
        'login': username,
        'passwd': password,
        'serv': servid,
        'code': code,
        'used': 1 if mark else 0
    }
    resp=nvp_request(endpoint,data,json=False).strip()
    if resp=='CLOSED':
        # Ok. All done
        return True
    elif resp=='ERROR':
        return False
    elif resp=='NOTUSER':
        raise Exception('Invalid credentials')
    else:
        # This should not pass except if remote api server is giving bad responses
        raise Exception('Unknown error')
    return resp