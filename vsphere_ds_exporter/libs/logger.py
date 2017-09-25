# -*- coding: utf-8 -*-
"""logging replacement of the standard logging library """
from __future__ import absolute_import, unicode_literals, division
import os

from logbook import Logger, FileHandler, set_datetime_format
from vsphere_ds_exporter import LOG_DIR


class ExporterLogger(object):

    ERROR_LOG_PATH = os.path.join(LOG_DIR, 'error.log')

    def __init__(self, logger_name):
        self.logger_name = logger_name
        set_datetime_format('local')

    def get_error_logger(self):
        error_logger = Logger(self.logger_name)
        file_handler = FileHandler(self.ERROR_LOG_PATH)
        file_handler.push_application()
        return error_logger

    def get_logger(self, logger_path):
        """
            logger configuration by logger name and log path
        :logger_name: the name of the logger
        :logger_path: log file location
        :return: logger of the log
        """
        info_logger = Logger(self.logger_name)
        log_file = os.path.join(LOG_DIR, logger_path)
        file_handler = FileHandler(log_file)
        file_handler.push_application()
        return info_logger
