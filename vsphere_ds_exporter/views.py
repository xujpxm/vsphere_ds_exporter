# -*- coding: utf-8 -*-
"""flask views file"""

from __future__ import absolute_import, unicode_literals
import logging
from datetime import datetime
from flask import Blueprint, render_template

from vsphere_ds_exporter.libs import vsphere
metrics = Blueprint('metrics', __name__)
logger = logging.getLogger('ds_exporter')


@metrics.route('/')
def index():
    return render_template('index.html')


@metrics.route('/metrics', methods=['GET'])
def details():
    start_time = datetime.now()
    # Get exporter datastores
    si = vsphere.connect_vc()
    logger.info('vCenter login success~')
    content = si.content
    vc_datacenters = vsphere.get_vc_dc(content)
    datastore = [n for n in vsphere.get_datastore(vc_datacenters)]
    logger.info('Datastore Query Starting')
    # Create a list of datastore and it's capacity/freespace/uncommited size string list
    capacity_list = ['vsphere_datastore_capacity_bytes{datastore=%s} %d'
                     % (ds.name, vsphere.get_ds_capacity(ds)) for ds in datastore]
    logger.info('Get datastore capacity size ok')
    free_list = ['vsphere_datastore_freespace_bytes{datastore=%s} %d'
                 % (ds.name, vsphere.get_ds_freespace(ds)) for ds in datastore]
    logger.info("Get free ds list is end")
    uncmtd_list = ['vsphere_datastore_uncommited_bytes{datastore=%s} %d'
                   % (ds.name, vsphere.get_ds_uncommitted(ds)) for ds in datastore]
    logger.info("Get uncommited ds list is end")
    vsphere.disconnect_vc(si)
    end_time = datetime.now()
    q_time = (end_time - start_time).seconds
    logger.info('Datastore Query Ending')
    logger.info('The Query time is {0}s'.format(q_time))
    return render_template('metrics.txt',  capacity_list=capacity_list,
                           free_list=free_list, ucmtd_list=uncmtd_list), {'Content-Type': 'text/plain'}
