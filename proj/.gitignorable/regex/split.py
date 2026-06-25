import re

string = "hi/i'm here/alone\with my\thougths/ for ever"


li = re.split(pattern=r'[\\/]',string=string)

print(li)