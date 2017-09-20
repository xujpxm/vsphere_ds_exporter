# -*- coding: utf-8 -*-
"""flask views file"""

from __future__ import absolute_import, unicode_literals
from flask import Blueprint, render_template

metrics = Blueprint('metrics', __name__)


@metrics.route('/')
def index():
    return render_template('index.html')


@metrics.route('/metrics')
def details():
    return render_template('metrics.html')
