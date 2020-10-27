# Python3


"""
Utils collection
Version 1.0
05.03.2020
"""


import logging
import json
import xml.etree.ElementTree as ET
from logging.handlers import RotatingFileHandler



""" Logger Configuration """

default_logging_name = 'utils'
default_logging_level = 20
FORMAT = '%(asctime)-15s %(levelname)s %(message)s'
formatter = logging.Formatter(FORMAT)
# Create handlers
c_handler = logging.StreamHandler()
f_handler = RotatingFileHandler('%s.log' % default_logging_name, mode='a', maxBytes=5*1024*1024, backupCount=2, encoding=None, delay=0)

# Create formatters and add it to handlers
c_handler.setFormatter(formatter)
f_handler.setFormatter(formatter)

logging.basicConfig(format=FORMAT, level=default_logging_level, handlers=[c_handler, f_handler])
logger = logging.getLogger(default_logging_name)
logger.setLevel(default_logging_level)









