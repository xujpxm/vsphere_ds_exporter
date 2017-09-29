# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division, absolute_import
import ssl
import os


class Config:
    """ vsphere env configuratioin"""
    VC_PORT = 443
    # vsphere login ssl setting
    CONTEXT = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    CONTEXT.verify_mode = ssl.CERT_NONE

    def __init__(self):
        pass


class ProConfig(Config):
    """ Production configuration"""
    DEBUG = False
    VC_USERNAME = ''
    VC_PASSWORD = ''
    VC_IP = os.environ.get('VC_IP', '1.1.1.1')


class DevConfig(Config):
    """ develogpment configuration"""
    DEBUG = True
    VC_USERNAME = 'administrator@yf.local'
    VC_PASSWORD = 'P@$$w0rd'
    VC_IP = os.environ.get('VC_IP', '172.16.0.4')


ENV_CONFIG = {
    'development': DevConfig,
    'production': ProConfig,
    'default': DevConfig
}
