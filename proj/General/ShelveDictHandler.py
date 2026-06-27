import shutil
from Loggers.g_logging import *
from General.DictHandler import *
import shelve
from General.SerializedInt import SerializedInt
from pathlib import Path
from EnvManager import force_get_env

class ShelveDictHandler(DictHandler):
    """
    Simulates a dict by shelf (shelve) aggregation
    """

    #TODO pull from .env
    #_path_to_running_id_storage: Path = Path(__file__).parent.parent / Path("files") / Path("running_shelves_id")
    _path_to_running_id_storage: Path = Path(force_get_env("RUNNING_SHELF_ID"))
    _running_id: SerializedInt = SerializedInt(_path_to_running_id_storage)


    _shelf_default_name = "shelf"

    #TOBEDONE from .env

    #_path_to_closet: Path = Path(__file__).parent / Path('closet_of_shelves')
    _path_to_closet: Path = Path(force_get_env("SHELVES_STORAGE_SPACE"))
    
    def __init__(self, name: str | None = None):
        #make sure the dir exists and is empty:
        if ShelveDictHandler._path_to_closet.exists():
            import shutil
            shutil.rmtree(ShelveDictHandler._path_to_closet)
        ShelveDictHandler._path_to_closet.mkdir(parents=True, exist_ok=True)
        name: str = name or ShelveDictHandler._shelf_default_name
        self.__name = f"{ShelveDictHandler._path_to_closet / Path(name)}_{ShelveDictHandler._running_id.val}"
        sh: shelve.Shelf = shelve.open(self.__name)
        sh.close()
        ShelveDictHandler._running_id.val += 1


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
                ret_val: tuple[KT, VT] = shelf[ShelveDictHandler._get_str_from_key(__key)]
                return ret_val[-1]
            except KeyError as e:
                # todo: log the error to specific place
                #g_logger.log(logging.ERROR, f"shelve: error {e}. with {__key =}. In {self.__name}")
                raise KeyError(e, f"tried to find {__key} in {self.__name}")


    def __len__(self) -> int:
        with shelve.open(self.__name) as sh:
            return len(sh)

    def __iter__(self) -> Iterator[KT]:
        with shelve.open(self.__name) as sh:
            for pair in sh.values():
                try:
                    yield pair[0]
                except (IndexError, TypeError, AttributeError) as e:
                    # TODO logging to the right place
                    g_logger.critical(f"at shelf with name {self.__name}, exception {e}. "
                                      f"probably the shelf values weren't the right format, aka ({KT},{VT})")

    @staticmethod
    def clear_closet(path_to_closet: Path):
        if path_to_closet.exists():
            shutil.rmtree(path_to_closet)
        path_to_closet.mkdir(parents=True, exist_ok=True)

if __name__ == '__main__':



    s2 = ShelveDictHandler("my")
    s4 = ShelveDictHandler("my")

