import logging

# Set the file name
logging.basicConfig(filename='my_log_file.log', 
					level=logging.INFO) 

def print_logs():
	logging.debug('I am a DEBUG level statement')
	logging.info('I am an INFO level statement')
	logging.warning('I am a WARNING level statement')
	logging.error('I am an ERROR level statement')
	logging.critical('I am a CRITICAL level statement')

# Default level is WARNING
# print_logs()

def log_something(x, y):
	try:
		logging.info("The value of var X is %d" % x)
		logging.info("The value of var Y is %d" % y)
		z = x + y
		logging.info("Their sum is %d", z)
	except TypeError as err:
		logging.error("Some error occurred!!")


log_something('abc', 20)