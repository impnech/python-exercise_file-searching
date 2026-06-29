from abc import *
from Loggers.g_logging import *


class Singleton(ABC):
    instances = {}

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls in Singleton.instances:
            return Singleton.instances[cls]

        g_logger.info(f"Class {cls.__name__} is creating a (single) instance for itself")
        new_cls: cls = super().__new__(cls)
        #new_cls: cls = super().__new__(*args, **kwargs)

        Singleton.instances[cls] = new_cls
        return Singleton.instances[cls]


if __name__ == '__main__':
    pass
