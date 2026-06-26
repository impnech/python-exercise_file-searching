import os
from dotenv import load_dotenv
print(f"{__file__.split("\\")[-1]} is being run")

# simple trick to 
dummy: None
try:
    dummy
except NameError:
    print("here")
    load_dotenv(override=True)



def force_get_env(key: str) -> str:
    res = os.getenv(key)
    if res is None:
        raise KeyError(f"{key=} doesn't exist in .env")
    return res

if __name__ == "__main__":
    x= force_get_env("DOCUMENTS_PATH")
    try:
        y = force_get_env("DOCUMENTS_PATH not")
        print("wrong")
    except:
        print("y failed succesfully")
    print(x,sep="\n")

