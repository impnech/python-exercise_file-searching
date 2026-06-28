import importlib

print(f"hi from {__file__.split('\\')[-1]}")
def foo():
    importlib.import_module("testing.imports_test.multi_import_test")
importlib.import_module("testing.imports_test.multi_import_test")
import testing.imports_test.multi_import_test
foo()

print(f"by from lib.py")