# -*- coding: utf-8 -*-
""" query vsphere datastore usage file"""
from __future__ import absolute_import, unicode_literals, division
import logging
import os
import atexit
import traceback

from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim

from config import ENV_CONFIG
CONFIG = ENV_CONFIG.get(os.environ.get('ENV_CONFIG', 'development'))
logger = logging.getLogger('ds_exporter')


def connect_vc():
    """
        vsphere loggin
    :param host: vCenter OR ESXI Server Address
    :param username: vCenter OR ESXI username
    :param password: password
    :return: vCenter or ESXI si(ServiceInstance)
    """
    try:
        si = SmartConnect(
            host=CONFIG.VC_IP,
            user=CONFIG.VC_USERNAME,
            pwd=CONFIG.VC_PASSWORD,
            port=CONFIG.VC_PORT,
            sslContext=CONFIG.CONTEXT)
        return si
    except vim.fault.InvalidLogin:
        logger.error(
            'Unable to login because of the invalid username and password!')
    except Exception:
        logger.error(traceback.format_exc())


def disconnect_vc(si):
    """
        disconnect vsphere
    :param si:
    :return:
    """
    try:
        atexit.register(Disconnect, si)
    except Exception:
        logger.error(traceback.format_exc())


def get_vc_dc(vc_content):
    """
        Get vcenter content datacenter
    :param vc_content: vCenter content
    :return: [datacenter object]
    """
    root_folder = vc_content.rootFolder
    dc_list = [datacenter for datacenter in root_folder.childEntity if isinstance(
        datacenter, vim.Datacenter)]
    return dc_list


def get_datastore(dc_list):
    """
        Get datacenter datastore object
    :param datacenter: vsphere datacenter object list
    :return: datastore object list
    """
    datastores = [datastore for dc in dc_list for datastore in dc.datastore]
    for ds in datastores:
        if not ds.summary.multipleHostAccess:
            # datastore must be access by multiple esxi host
            continue
        if 'qrm'.upper() in ds.name.upper():
            # exclude 'QRM' in datastore name
            continue
        if ds.summary.type != 'VMFS':
            # must be vmfs file type
            continue
        logger.info('Get vcenter datastore %s success~' % ds.name)
        yield ds


def get_ds_capacity(datastore):
    """
        Get vsphere datastore capacity size
    :param datastore: vsphere datastore object
    :return: datastore capacity size
    """
    capacity_size = datastore.summary.capacity
    return capacity_size


def get_ds_freespace(datastore):
    """
        Get vsphere datastore freeSpace size
    :param datastore: vsphere datastore object
    :return: datastore freeSpace size
    """
    freespace_size = datastore.summary.freeSpace
    return freespace_size


def get_ds_uncommitted(datastore):
    """
        Get vsphere datastore uncommitted size
    :param datastore: vsphere datastore object
    :return: datastore uncommitted size
    """
    uncommitted_size = datastore.summary.uncommitted
    return uncommitted_size
