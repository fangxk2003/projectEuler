def check(x) :
    vis = [0 for i in range(0, 10)]
    vis[0] = 1
    while(x > 0) :
        if vis[x % 10] : return(0)
        vis[x % 10] = 1
        x = x // 10
    return(1)

ans = 0
for i in range(1, 10000) :
    x = i
    st = str(x) + str(x * 2)
    now = 2
    while (len(st) < 9) :
        now += 1
        st = st + str(x * now)
    if (len(st) == 9) :
        val = int(st)
        if (check(val)) :  ans = max(ans, val)
print(ans)