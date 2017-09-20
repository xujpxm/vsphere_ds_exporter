# -*- coding: utf-8 -*-
""" vsphere datastore expoter for prometheus init file """

from __future__ import absolute_import, unicode_literals
from flask import Flask

from vsphere_ds_exporter.views import metrics

app = Flask(__name__)
app.register_blueprint(metrics)
