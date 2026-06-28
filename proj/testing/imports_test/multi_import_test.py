import os
import importlib
# api_key = os.environ
# print(api_key)

# import testing.imports_test.multi_import2 
# import testing.imports_test.multi_import3
from EnvManager import force_get_env
import EnvManager
importlib.reload(EnvManager)

x = importlib.import_module("testing.imports_test.lib")

print(f"hi from {__file__.split('\\')[-1]}")

foo = getattr(x,"foo")


foo()

print(f"bye from {__file__.split("\\")[-1]}")