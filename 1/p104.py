from math import log10
def ck(x) :
    vis = [0 for i in range(0, 10)]
    vis[0] = 1
    for _ in range(0, 9) :
        if (vis[x % 10]) : return(0)
        vis[x % 10] = 1
        x = x // 10
    return(1)

f0 = 0
f1 = 1
now = 2
for i in range(0, 2000) :
    f2 = f0 + f1
    f0 = f1
    f1 = f2
now = 2002

while 1 :
    f2 = f0 + f1
    if (ck(f2 % 1000000000) and ck(f2 // (10 ** (int(log10(f2)) - 8)))) :
        print(now)
        exit()
    f0 = f1
    f1 = f2
    now += 1
