from random import randint, randrange
import json

if 0.200234 + 0.220022 == 0.420256:
    print("good for you")
else:
    print("haha")

goods=[];bads=[]
x = y = the_sum = "0."
for _ in range(100):
    for _ in range(randint(1,4)):
        xd=randint(0,4)
        yd=randint(0,4)
        #xd = 1
        #yd = 2
        the_sumd = yd + xd
        x += str(xd)
        y += str(yd)
        the_sum += str(the_sumd)

    xf = float(x);
    yf = float(y);
    the_sumf = float(the_sum)

    #print(xf, yf, the_sumf)
    if xf + yf == the_sumf:
        goods.append((xf,yf))
    else:
        bads.append((xf,yf))
    #print(f"{float(x)=}, {float(y)=}, {float(the_sum)=}")

fname="saved_bad_floaties"

if not bads: quit()
print(f"writing {bads} to {fname}")
f=open(fname,'a')
print(*bads,file=f)
