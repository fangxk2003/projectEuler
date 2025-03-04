def ck(x) :
    vis = [0 for i in range(0, 10)]
    vis[8] = vis[9] = 1
    vis[0] = 1
    while x > 0 :
        if (vis[x % 10]) : return(0)
        vis[x % 10] = 1
        x = x // 10
    return(1)

def isP(x) :
    for i in range(2, int(x ** 0.5) + 1) :
        if (x % i == 0) : return(0)
    return(1)

for i in range(10000000, 0, -1) :
    if ck(i) and isP(i) :
        print(i)
        exit()