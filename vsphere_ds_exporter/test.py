# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division, absolute_import

import logging
from flask import Blueprint
from flask import Response

test = Blueprint('test', __name__)
logger = logging.getLogger('ds_exporter')


@test.route('/')
def details():
    str = """# HELP vsphere_datastore_capacity datastore capacity\n# TYPE vsphere_datastore_capacity gauge
vsphere_datastore_capacity_bytes{name="NYFCLOUD-TYPE03-VOL"} 1145414090752
vsphere_datastore_freespace_bytes{name="NYFCLOUD-TYPE03-VOL"} 150457024512
vsphere_datastore_uncommitted_bytes{name="NYFCLOUD-TYPE03-VOL"} 5498350192533
    """
    return Response(str, mimetype='text/plain')
