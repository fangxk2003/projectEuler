import numpy as np
def calc(n, k, flag):
    t = np.ones(n, dtype=int)
    s = np.ones(n, dtype=int)
    trans = np.zeros((n, n), dtype=int)
    for i in range(n) : 
        if i == 0 : trans[0][1] = 1
        elif i == n - 1 : trans[n - 1][n - 2] = 1
        else : trans[i][i - 1] = trans[i][i + 1] = 1
    
    for i in range(k - 1) :
        t = trans @ t
        s = s + t
    if flag == 0 : return s[1:].sum()
    else : return s.sum()

print(calc(10, 40, 0) - calc(9, 40, 0) - calc(9, 40, 1) + calc(8, 40, 1))