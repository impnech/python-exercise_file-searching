import logging
import os
from EnvManager import force_get_env


_path = force_get_env()
g_logger: logging.Logger = logging.getLogger("global_logger")
#TODO make this absolute in config
logging.basicConfig(
    filename=f"{_path}/global_logging.log",
    filemode='a',
    level=logging.DEBUG,
    format="%(levelname)s, %(module)s, %(asctime)s,  %(message)s  -  %(name)s"
)

if __name__ == '__main__':
    print(_path)
