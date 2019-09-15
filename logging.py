import logging
import logging.handlers

# Settings
# Generic logging parameters
LOG_NAME = __name__
LOG_DATE_FORMAT = '%Y-%m-%d %H:%m'
# Logging config parameters for console
LOG_FORMAT_CONSOLE = '%(asctime)s [%(levelname)5s] [%(name)s] [%(filename)s:%(lineno)d] %(message)s'
LOG_LEVEL_CONSOLE = 'DEBUG'
# Logging config parameters for file
LOG_FILENAME = "logfile.log"
LOG_FORMAT_FILE = '%(asctime)s [%(levelname)5s] [%(name)s] [%(filename)s:%(lineno)d] %(message)s'
LOG_LEVEL_FILE = 'DEBUG'LOG_LEVEL_FILE = logging.DEBUG

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(LOG_LEVEL_CONSOLE)

# Create a file handler
file_handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=1048576, backupCount=2)
file_handler.setLevel(LOG_LEVEL_FILE)

# Set format to handlers
formatter_console = logging.Formatter(fmt=LOG_FORMAT_CONSOLE,datefmt=LOG_DATE_FORMAT)
formatter_file = logging.Formatter(fmt=LOG_FORMAT_FILE,datefmt=LOG_DATE_FORMAT)
console_handler.setFormatter(formatter_console)
file_handler.setFormatter(formatter_file	)

# Create the logger and add handlers
log = logging.getLogger(LOG_NAME)
log.addHandler(console_handler)
log.addHandler(file_handler)


log.debug("logging settings completed")
