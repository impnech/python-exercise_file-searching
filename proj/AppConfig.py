import json
from EnvManager import force_get_env
from pathlib import Path
from Loggers import g_logging

_config_cache = None

def get_config():
    """
    Returns the application configuration, loading it if not already cached.
    """
    global _config_cache
    
    if _config_cache is None:
        project_root = force_get_env("ROOTPATH")
        config_path = force_get_env("CONFIG_PATH")

        try:
            with open(config_path, "r") as file:
                _config_cache = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # Fallback or default values if file is missing/broken
            _config_cache = {
                "dict_handler": {
                    "module_path": "Storage.Handlers",
                    "class_name": "SimpleDictHandler"
                }
            }
            
    return _config_cache

def get_setting(key, default=None):
    """Helper to fetch a specific top-level configuration setting."""
    return get_config().get(key, default)