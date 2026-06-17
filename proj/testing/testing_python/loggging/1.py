import logging
from logging import getLogger

logging.basicConfig(filename="try_log")
logging.log(logging.CRITICAL, "i was wrong")
my_logger = getLogger("littlelogger")

my_logger.log(4, "hi")
my_logger.log(logging.ERROR, "hi3")

my_logger.debug("bug?")


my_logger.error("hi4")
# print(my_logger.error("error"))


