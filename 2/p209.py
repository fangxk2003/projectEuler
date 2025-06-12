from collections import deque
import copy
import numpy as np
k = 6
t = 2 ** 6
ori = set()
cp = [set() for _ in range(t)]
vis = [False] * t
for st in range(t) :
    o = []
    for i in range(k) :
        o.append((st >> i) & 1)
    st_new = (st >> 1) | ((o[0] ^ (o[1] & o[2])) << 5)
    if st == st_new : ori.add(st)
    else :
        cp[st_new].add(st)
        cp[st].add(st_new)


lp = []
for i in range(1, t) :
    if not vis[i] : 
        now = i
        cnt = 1
        vis[i] = True
        while True :
            flag = False
            for j in cp[now] :
                if not vis[j] :
                    now = j
                    vis[j] = True
                    flag = True
                    break
            if not flag : break
            cnt += 1
        lp.append(cnt)
lp.sort()
print(lp)

f = [np.zeros((2, 2), int)]
mul = np.ones((2, 2), int)
f[-1][0, 0] = f[-1][1, 1] = 1
mul[1, 1] = 0
for i in range(45) :
    f.append(f[-1] @ mul)

res = 1
for x in lp :
    res *= f[x - 1][0, 0] + f[x - 1][0, 1] + f[x - 1][1, 0]
print(res)

# 4106118286
# 15964587728784

# mul = 0
# for o in ori :
#     vis[o] = True
#     for i in cp[o] : 
#         cp[i].remove(o)
# for i in range(t) :
#     if not cp[i]:
#         vis[i] = True
#         mul += 1
# print(mul)
# def srch(x) :
#     global vis, cp
#     cnt = 0
#     vis[x] = True
#     V = vis.copy()
#     CP = copy.deepcopy(cp)
#     # tau[x] = 1
#     mul = 0
#     for i in CP[x] :
#         vis[i] = True
#         mul += update(i)
#     flag = False
#     for j in range(x + 1, t) :
#         if not vis[j] :
#             cnt += srch(j) * 2 ** mul
#             flag = True
#             break
#     if not flag : cnt += 2 ** mul
#     # tau[x] = 0
#     cp = CP.copy()
#     mul = update(x)
#     flag = False
#     for i in range(t) :
#         if not vis[i] :
#             cnt += srch(i) * 2 ** mul
#             flag = True
#             break
#     if not flag : cnt += 2 ** mul
#     vis = V.copy()
#     cp = CP.copy()
#     return cnt

# for i in range(t) :
#     if not vis[i] :
#         res = srch(i) * 2 ** mul
#         print(res)
#         break


