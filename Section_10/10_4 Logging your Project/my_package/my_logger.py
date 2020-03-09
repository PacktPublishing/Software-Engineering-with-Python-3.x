import logging

format_string = '%(asctime)s:%(filename)s_%(levelname)s:::%(message)s'
log_file_name = 'my_package_logs.log'

logger = logging.getLogger(__name__)
logger.setLevel('INFO')

# Use a FileHandler()
file_handler = logging.FileHandler(log_file_name)
log_formatter = logging.Formatter(format_string)
file_handler.setFormatter(log_formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)