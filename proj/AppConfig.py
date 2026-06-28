import json
import importlib
from EnvManager import force_get_env
from pathlib import Path
#will create circular import: from Loggers import g_logging

class ConfigException(FileNotFoundError,json.JSONDecodeError):
    pass


_config_cache = None

def get_config():
    """
    Returns the application configuration, loading it if not already cached.
    """
    global _config_cache
    
    if _config_cache is None:
        #project_root = force_get_env("ROOTPATH")
        config_path = force_get_env("CONFIG_PATH")

        try:
            with open(config_path, "r") as file:
                _config_cache = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e: 
            raise ConfigException(f"config didn't load properly. with error: {e}")
            
    return _config_cache

def get_setting(key, default=None):
    """Helper to fetch a specific setting."""
    return get_config().get(key, default)

def force_get_setting(key):
    """Helper to fetch a specific setting, with confidance that it exists, (otherwise throws)"""   
    try:
        return get_config()[key]
    except KeyError:
        raise KeyError(f"config doesn't have the setting {key}")

def get_class_implementation(type_to_create: str) -> type:
    impl_dict = force_get_setting("implementations")[type_to_create]
    module_path: str = impl_dict["module_path"]
    class_name: str = impl_dict["class_name"]
    module = importlib.import_module(module_path)
    cls = getattr(module, class_name)
    return cls

from collections import deque

def get_class_implementations_list(cls: str)->list[type]:
    impl_dicts = force_get_setting("implementations_lists")[cls]
    res = deque()
    for impl_dict in impl_dicts:
        module_path: str =  impl_dict["module_path"]
        class_name: str = impl_dict["class_name"]
        module = importlib.import_module(module_path)
        cls = getattr(module, class_name)
        res.append(cls)
    return list(res)
    

def get_default_value(name: str)->any:
    value_d: dict = force_get_setting("default_values")
    value = value_d[name]
    return value

def get_outside_variable(name: str):
    vars = force_get_setting("outside_variables")
    value = vars[name]
    return value

if __name__ == "__main__":
    sett = force_get_setting("implementations_lists")['StringStreamTransformer']
    print(f"{sett=}")
    exit()
    v= get_default_value("splitter_delimiter")
    print(f"{v=}")
    for s in ["DictHandler", "Calculator"]:
        x = get_class_implementation(s)
        print(f"{type(x)=}\n{x=}")
    pass   

