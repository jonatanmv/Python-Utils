import logging
import logging.handlers
import os

from pathlib import Path

# Settings
# Generic logging parameters
LOG_TO_FILE = True
LOG_TO_CONSOLE = True
LOG_NAME = __name__
LOG_DATE_FORMAT = '%Y-%m-%d %H:%m'
# Logging config parameters for console
LOG_FORMAT_CONSOLE = '%(asctime)s [%(levelname)5s] [%(name)s] [%(filename)s:%(lineno)d] %(message)s'
LOG_LEVEL_CONSOLE = 'DEBUG'
# Logging config parameters for file
FILANEME_WITHOUT_EXTENSION = Path(__file__).with_suffix('').stem
LOG_FILENAME = FILANEME_WITHOUT_EXTENSION+"log"
LOG_FORMAT_FILE = '%(asctime)s [%(levelname)5s] [%(name)s] [%(filename)s:%(lineno)d] %(message)s'
LOG_LEVEL_FILE = 'DEBUG'LOG_LEVEL_FILE = logging.DEBUG

# Set format to handlers
formatter_console = logging.Formatter(fmt=LOG_FORMAT_CONSOLE,datefmt=LOG_DATE_FORMAT)
formatter_file = logging.Formatter(fmt=LOG_FORMAT_FILE,datefmt=LOG_DATE_FORMAT)

# Create a console handler
if LOG_TO_CONSOLE:
  console_handler = logging.StreamHandler()
  console_handler.setLevel(LOG_LEVEL_CONSOLE)
  console_handler.setFormatter(formatter_console)
  
# Create a file handler
if LOG_TO_FILE:
  file_handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=1048576, backupCount=2)
  file_handler.setLevel(LOG_LEVEL_FILE)
  file_handler.setFormatter(formatter_file)

# Create the logger and add handlers
log = logging.getLogger(LOG_NAME)
log.addHandler(console_handler)
log.addHandler(file_handler)


log.debug("logging settings completed")
