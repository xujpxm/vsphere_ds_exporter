# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division, absolute_import

import logging
from flask import Blueprint
from flask import Response

test = Blueprint('test', __name__)
logger = logging.getLogger('ds_exporter')


@test.route('/')
def test_index():
    logger.debug('lalalallaal')
    logger.info('iinfo lalalallaal')
    logger.error('error lalalallaal')
    return 'test hello world'
