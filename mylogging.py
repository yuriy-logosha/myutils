# Python3


"""
Utils collection
Version 1.0
05.03.2020
"""


import logging
import json
import xml.etree.ElementTree as ET



""" Logger Configuration """

default_logging_name = 'utils'
default_logging_level = 20
FORMAT = '%(asctime)-15s %(levelname)s %(message)s'
formatter = logging.Formatter(FORMAT)
# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('%s.log' % default_logging_name)

# Create formatters and add it to handlers
c_handler.setFormatter(formatter)
f_handler.setFormatter(formatter)

logging.basicConfig(format=FORMAT, level=default_logging_level, handlers=[c_handler, f_handler])
logger = logging.getLogger(default_logging_name)
logger.setLevel(default_logging_level)









