# demonstrate the logging api in Python

# TODO: use the built-in logging module
import logging
from test import test_log

# TODO: Use basicConfig to configure logging
logging.basicConfig(level=logging.DEBUG, 
                    filename='output.log', 
                    filemode='w', 
                    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s %(funcName)s - %(lineno)d: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S') # DEBUG, INFO, WARNING, ERROR, CRITICAL

# TODO: Try out each of the log levels
logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")
x = "TextString"
y = 999
logging.info(f"Here's a {x} variable and an int: {y}")
# TODO: Output formatted strings to the log
def main():
    logging.error("A main function error message")
    test_log()


main()