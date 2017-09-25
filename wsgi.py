#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" project wsgi file"""

from __future__ import absolute_import, unicode_literals, division

from vsphere_ds_exporter import app

if __name__ == '__main__':
    app.debug = True
    app.run()
