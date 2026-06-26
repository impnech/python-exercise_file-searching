import os
pa = os.getenv("STOPWORDS_FILE_PATH")

print(f"{pa=}")

try:
    with open(pa) as stopwords:
        print(stopwords.read())
except :
    print(f" path {pa} didn't open")