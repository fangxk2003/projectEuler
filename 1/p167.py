import numpy as np
from utils import matrix_quick_power
k = 10 ** 11
ans = 0
for n in range(2, 11) :
    pd = 2 * n + 2
    mat = np.zeros((pd, pd), int)
    for i in range(pd - 1) : mat[i + 1][i] = 1
    mat[0][pd - 1] = mat[pd - 1][pd - 1] = 1
    now = np.ones((1, pd), int)
    lp = 0
    num = 0
    while(1) :
        now = now @ mat
        now = now & 1
        num += now[0][pd - 1]
        lp += 1
        if np.all(now == 1): break
    print(n, num, lp)
    res = n - 1 + pd + (k - 2 - pd) // num * lp
    r = (k - 2 - pd) % num
    lp = 0
    num = 0
    now = np.ones((1, pd), int)
    while(1) :
        now = now @ mat
        now = now & 1
        num += now[0][pd - 1]
        lp += 1
        if num == r : break
    res += lp
    ans += res * 2 + 1
    print(res)
print(ans)
    