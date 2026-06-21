from Loggers.g_logging import *
from DictHandler import *
import shelve


class ShelveDictHandler(DictHandler):
    """
    Simulates a dict by shelf (shelve) aggregation
    """
    _running_id: int = 1
    _shelf_name = "shelf"

    def __init__(self, name: str | None = None):

        if not name:
            name = ""
        self.__name = f"{name}{ShelveDictHandler.shelf_name}{ShelveDictHandler.running_id}"
        sh: shelve.Shelf = shelve.open(self.__name)
        sh.close()
        ShelveDictHandler.running_id += 1


    @staticmethod
    def _get_str_from_key(k: KT):
        """
        Since the shelve module expects the key to have the key of type string.
        And we can't have be sure that str(k) will give something unique, str(hash(k)) seems like an acceptable compromise
        """
        return str(hash(k))

    f"""
    Regardless, of how {_get_str_from_key.__name__} works, we need to be able to access the original key
    """
    def __setitem__(self, key: KT, value: VT):
        with shelve.open(self.__name) as shelf:
            shelf[ShelveDictHandler._get_str_from_key(key)]: tuple[KT, VT] = (key, value)

    def __getitem__(self, __key: KT) -> VT:
        with shelve.open(self.__name, "r") as shelf:
            try:
                ret_val: tuple[KT,VT] = shelf[ShelveDictHandler._get_str_from_key(__key)]
            except KeyError as e:
                # TODO: log the error to specific place
                g_logger.log(logging.ERROR, f"shelve: error {e}. with {__key =}. In {self.__name}")
            return ret_val[-1]

    def __len__(self) -> int:
        with shelve.open(self.__name) as sh:
            return len(sh)

    def __iter__(self) -> Iterator[KT]:
        with shelve.open(self.__name) as sh:
            for pair in sh.values():
                try:
                    yield pair[0]
                except (IndexError,TypeError,AttributeError) as e:
                    # TODO logging to the right place
                    g_logger.critical(f"at shelf with name {self.__name}, exception {e}. "
                                      f"probably the shelf values weren't the right format, aka ({KT},{VT})")


if __name__ == '__main__':
    s1 = ShelveDictHandler()
    s2 = ShelveDictHandler("shelf1")

