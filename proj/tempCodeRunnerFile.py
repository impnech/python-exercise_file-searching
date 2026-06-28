def get_class_implementations_list(cls: str)->list[type]:
#     impl_dicts = force_get_setting("implementations_lists")[cls]
#     res = deque()
#     for impl_dict in impl_dicts:
#         module_path: str =  impl_dict["module_path"]
#         class_name: str = impl_dict["class_name"]
#         module = importlib.import_module(module_path)
#         cls = getattr(module, class_name)
#         res.append(cls)
#     return list(res)
    