import logging
import os
from EnvManager import force_get_env


_path = force_get_env("GLOBAL_LOGGER_PATH")
logger_filename:str = force_get_env("GLOBAL_LOGGER_PATH")
g_logger: logging.Logger = logging.getLogger("global_logger")
#TODO make this absolute in config
logging.basicConfig(
    filename=logger_filename,
    filemode='a',
    level=logging.DEBUG,
    format="%(levelname)s, %(module)s, %(asctime)s,  %(message)s  -  %(name)s"
)

if __name__ == '__main__':
    print(_path)
