#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" project wsgi file"""

from __future__ import absolute_import, unicode_literals, division
import os
from vsphere_ds_exporter import app
from config import ENV_CONFIG
CONFIG = ENV_CONFIG.get(os.environ.get('ENV_CONFIG', 'development'))

if __name__ == '__main__':
    app.debug = CONFIG.DEBUG
    app.run()
