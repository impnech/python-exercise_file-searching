from Loggers.g_logging import g_logger

class DefaultHolder:
    @property
    def default_value(self):
        return self.__default_value
    
    def __init__(self, default_value):
        self.__default_value = default_value