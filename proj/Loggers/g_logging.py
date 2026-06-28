import logging
import os
from EnvManager import force_get_env, get_absolute_path
from AppConfig import force_get_setting


_path = get_absolute_path("GLOBAL_LOGGER_PATH")
logger_filename:str = force_get_env("GLOBAL_LOGGER_PATH")
g_logger: logging.Logger = logging.getLogger("global_logger")

#TODO make this absolute in config?
partial_setting: dict[str, str] = force_get_setting("g_logger_partial_settings")
logging.basicConfig(
    filename=logger_filename,
    level=logging.DEBUG,

    **partial_setting,
    #filemode='a',
    #format="%(levelname)s, %(module)s, %(asctime)s,  %(message)s  -  %(name)s",
)

if __name__ == '__main__':
    print(_path)
    g_logger.info("g_logger initiatted succesfully")
