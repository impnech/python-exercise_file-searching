import os
import importlib
api_key = os.environ
print(api_key)

import testing.multi_import2 
import testing.multi_import3
from EnvManager import force_get_env
import EnvManager
importlib.reload(EnvManager)