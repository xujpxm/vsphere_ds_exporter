# -*- coding: utf-8 -*-
""" flask manager file"""

from __future__ import absolute_import, unicode_literals
from flask_script import Manager
from vsphere_ds_exporter import app

app.debug = True
manager = Manager(app)

if __name__ == "__main__":
    manager.run()
