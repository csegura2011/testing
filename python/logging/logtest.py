#!/usr/bin/pythonn
# logging package testing

import logging

# Example 001
# -----------
LOG_FILENAME='example.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
logging.debug('This message shild go to the log file')
# ---------
# example.log
#   DEBUG:root:This message shild go to the log file
