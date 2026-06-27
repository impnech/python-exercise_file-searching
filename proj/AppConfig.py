import json
from EnvManager import force_get_env
from pathlib import Path
from Loggers import g_logging

class ConfigException(FileNotFoundError,json.JSONDecodeError):
    pass


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
        except (FileNotFoundError, json.JSONDecodeError) as e: 
            raise ConfigException(f"config didn't load properly. with error: {e}")
            
    return _config_cache

def get_setting(key, default=None):
    """Helper to fetch a specific top-level configuration setting."""
    return get_config().get(key, default)