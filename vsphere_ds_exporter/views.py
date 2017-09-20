# -*- coding: utf-8 -*-
"""flask views file"""

from __future__ import absolute_import, unicode_literals
from flask import Blueprint, render_template
from flask import Response

metrics = Blueprint('metrics', __name__)


@metrics.route('/')
def index():
    return render_template('index.html')


@metrics.route('/metrics')
def details():
    str = """# HELP vsphere_datastore_capacity datastore capacity
# TYPE vsphere_datastore_capacity gauge
vsphere_datastore_capacity_bytes{name="NYFCLOUD-TYPE03-VOL"} 1145414090752
vsphere_datastore_freespace_bytes{name="NYFCLOUD-TYPE03-VOL"} 150457024512
vsphere_datastore_uncommitted_bytes{name="NYFCLOUD-TYPE03-VOL"} 5498350192533
    """
    return Response(str, mimetype='text/plain')
