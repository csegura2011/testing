#!/usr/bin/pythonn
# logging package testing

import glob
import logging
import logging.handlers


# Example 002
# -----------
LOG_FILENAME = 'logging_rotatingfile_example.out'
# Set up a specific logger with out desired output level
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)
# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=20, backupCount=5)
my_logger.addHandler(handler)
# Log some messages
for i in range(20):
    my_logger.debug('i = %d' % i)
# See what files are created
logfiles = glob.glob('%s*' % LOG_FILENAME)

for filename in logfiles:
    print filename
#----------------
# Resultados
#     logging_rotatingfile_example.out
#     logging_rotatingfile_example.out.1
#     logging_rotatingfile_example.out.2
#     logging_rotatingfile_example.out.3
#     logging_rotatingfile_example.out.4
#     logging_rotatingfile_example.out.5