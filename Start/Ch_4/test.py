import logging

def test_log():
    logging.debug("This is a debug message")
    logging.info("This is a info message")
    logging.warning("This is a warning message")
    logging.error("This is a error message")
    logging.critical("This is a critical message")
    x = "FromTestFile"
    y = 777
    logging.info(f"Here's a {x} string and an integer: {y}")
