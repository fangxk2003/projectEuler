ans = 0

def check(v) :
    return len(set(str(v))) == 10

def sc(st, x, t, val, bas) :
    global ans
    # print(st, x, t, val, bas)
    if x == 10 :
        if t >= 1 and check(val) and val > ans :
            ans = val
            print(st, val)
        return
    if t == 4 : return 
    for i in range(x + 1, 11) :
        if t == 0 : sc(st, i, t + 1, 0, int(st[x:i]))
        else : sc(st, i, t + 1, val + bas * int(st[x:i]), bas)

def src(vis, num) :
    if len(num) == 10 :
        sc(num, 0, 0, 0, 0)
        return
    for i in range(9, -1, -1) :
        if not vis[i] :
            vis[i] = True
            src(vis, num + str(i))
            vis[i] = False

ans = 0
src([False for i in range(10)], "")
