# 28684

def sum(x0, y, id) :
    # print(x0, y, id)
    if (id == 6) :
        if (x0 == y) : return 1
        else : return 0
    for i in range(6) :
        if (not flag[i]) :
            flag[i] = True
            for z in nxt[i][y] :
                s = sum(x0, z, id + 1)
                if (s) : return s + y * 100 + z
            flag[i] = False
    return 0

# nxt = [[[]] * 100] * 6 # list is linked
nxt = [[[] for _ in range(100)] for __ in range(6)]
flag = [False for _ in range(6)]
for n in range(10, 200) :
    p = [n * (n + 1) // 2, n ** 2, n * (n * 3 - 1) // 2, n * (n * 2 - 1), n * (n * 5 - 3) // 2, n * (n * 3 - 2)]
    # print(p)
    for i in range(6) :
        l = p[i] // 100
        r = p[i] % 100
        if (l >= 10 and l < 100 and r >= 10) :
            nxt[i][l].append(r)
            # print(len(nxt[0][0]))
# print(len(nxt[0][0])) 

for x in range(10, 100) :
    s = sum(x, x, 0)
    if (s) :
        print(s - 1)
        exit()