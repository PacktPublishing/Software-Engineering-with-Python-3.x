import logging

# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=10)

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=20)

def print_logs():
	logging.debug('I am a DEBUG level statement')
	logging.info('I am an INFO level statement')
	logging.warning('I am a WARNING level statement')
	logging.error('I am an ERROR level statement')
	logging.critical('I am a CRITICAL level statement')

# Default level is WARNING
print_logs()