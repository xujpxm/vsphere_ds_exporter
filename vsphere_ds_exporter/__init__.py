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


logging_setting = {
    # logging configuration
    "version": 1,
    "formatters": {
        "simple": {
            "format": "[%(asctime)s] %(levelname)s: %(name)s: %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "exporter": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": os.path.join(LOG_DIR, 'vsphere_ds_exporter.log'),
            "when": "midnight",
            "backupCount": 30
        },
    },
    "loggers": {
        "console": {
            "level": "DEBUG",
            "handlers": [
                "console"
            ],
            "propagate": False
        },
        "ds_exporter": {
            "level": "DEBUG",
            "handlers": [
                "exporter",
            ],
            "propagate": False
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "console",
            "exporter"
        ],
    }
}


logging.config.dictConfig(logging_setting)
