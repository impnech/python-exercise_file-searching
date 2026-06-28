import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(override=True)

#print(f"{__file__.split("\\")[-1]} is being run")


def get_root_path() -> str:
    return force_get_env("ROOTPATH")

def get_absolute_path(name_or_rel_path: str | Path) -> Path:
    rel_path: str = os.getenv(name_or_rel_path)
    if rel_path is None:
        rel_path = name_or_rel_path
    root_p = Path(get_root_path())
    return root_p / rel_path

def force_get_env(key: str) -> str:
    res = os.getenv(key)
    if res is None:
        raise KeyError(f"{key=} doesn't exist in .env")
    return res

if __name__ == "__main__":
    x= force_get_env("DOCUMENTS_PATH")
    try:
        y = force_get_env("DOCUMENTS_PATH_not")
        print("wrong")
    except:
        print("y failed succesfully")
    print(x,sep="\n")

