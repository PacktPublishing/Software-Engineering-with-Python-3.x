import logging
import time

# See the full list of attributes here:
# https://docs.python.org/3/library/logging.html#logrecord-attributes

# Simple Time and Message format
# format_string = '%(asctime)s %(message)s'

# Simple Time, Function and Message format
# format_string = '%(filename)s %(funcName)s %(message)s'

# Time, Filename, Line No. and Message
# format_string = '%(asctime)s:%(filename)s_%(lineno)d:%(message)s'

# Time, Level Name and Message
format_string = '%(asctime)s: %(levelname)s:::%(message)s'

logging.basicConfig(filename='my_log_file.log', 
					level=logging.INFO, 
					format=format_string, 
					filemode='w')  

def print_logs():
	logging.debug('I am a DEBUG level statement')
	time.sleep(1)
	logging.info('I am an INFO level statement')
	time.sleep(1)
	logging.warning('I am a WARNING level statement')
	time.sleep(1)
	logging.error('I am an ERROR level statement')
	time.sleep(1)
	logging.critical('I am a CRITICAL level statement')

# Default level is WARNING
print_logs()

def log_something(x, y):
	logging.info("The value of var X is %d" % x)
	logging.info("The value of var Y is %d" % y)
	z = x + y
	logging.info("Their sum is %d", z)

log_something(10, 20)