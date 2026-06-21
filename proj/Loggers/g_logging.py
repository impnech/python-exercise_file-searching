import logging
import os



_path = os.path.dirname(os.path.realpath(__file__))
g_logger: logging.Logger = logging.getLogger("global_logger")
#TODO make this absolute in config
logging.basicConfig(filename=f"{_path}/global_logging.log", filemode='a', level=logging.DEBUG)

if __name__ == '__main__':
    print(_path)
