from Dicts.DictHandler import *
from AppConfig import get_class_implementation
from Loggers.g_logging import g_logger

# tobedo better (config)
class DictHandlerFactory:
    # towantdo: allow a choice of dicts, depending on the situation

    fetch_string= DictHandler.__name__
    @staticmethod
    def get_dict_handler() -> DictHandler:
        dict_handler_class = get_class_implementation(DictHandlerFactory.fetch_string)
        g_logger.debug(f"dict_handler factory initiated: {dict_handler_class}")
        return dict_handler_class()
    
    @staticmethod
    def get_dict_handler_by_class_name(class_name:str,):
        raise NotImplementedError()
    

if __name__ == "__main__":
    x = DictHandlerFactory.get_dict_handler()
    print(f"{type(x)=}, {x}")