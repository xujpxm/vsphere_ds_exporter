# -*- coding: utf-8 -*-
""" query vsphere datastore usage file"""
from __future__ import absolute_import, unicode_literals, division
import ssl

from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
from libs.logger import logger_config

vsphere_logger = logger_config('vsphere', 'vsphere.log')
# ssl context
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.verify_mode = ssl.CERT_NONE


def connect_vc(host, username, password):
    """
        vsphere loggin
    :param host: vCenter OR ESXI Server Address
    :param username: vCenter OR ESXI username
    :param password: password
    :return: vCenter or ESXI si
    """
    try:
        si = SmartConnect(
            host=host,
            user=username,
            pwd=password,
            port=443,
            sslContext=context)
        return si
    except vim.fault.InvalidLogin:
        raise LoginException(u'由于用户名或密码不正确，无法完成登录。')


def disconnect_vc(si):
    """
        disconnect vsphere
    :param si:
    :return:
    """
    try:
        Disconnect(si)
        sock = si._stub.pool[0][0]._wrapped.sock
        sock.close()
    except Exception as e:
        raise DisconnectVcException(u"disconnect vc error ....")


def get_vc_dc(vc_content):
    """
        获取指定content的数据中心
    :param vc_content: vCenter content
    :return: datacenter object
    """
    dc_list = []
    root_folder = vc_content.rootFolder
    for dc in root_folder.childEntity:
        if isinstance(dc, vim.Datacenter):
            dc_list.append(dc)
    return dc_list
