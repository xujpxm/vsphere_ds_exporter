# -*- coding: utf-8 -*-
""" vsphere datastore expoter for prometheus init file """

from __future__ import absolute_import, unicode_literals, print_function
import os
import traceback
import logging
import logging.config
import yaml
from flask import Flask

from vsphere_ds_exporter.views import metrics
from vsphere_ds_exporter.test import test

app = Flask(__name__)
app.register_blueprint(metrics)
app.register_blueprint(test, url_prefix='/test')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, 'logs')


def log_setup():
    """ log config"""
    log_conf_path = os.path.join(BASE_DIR, 'log.yml')
    try:
        with open(log_conf_path, 'r') as f:
            logging.config.dictConfig(yaml.load(f))
    except Exception:
        print(traceback.format_exc())
        # print("log config file is not found")


log_setup()
