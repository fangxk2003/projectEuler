import numpy as np
vis = np.zeros((5,) + (15,) * 5, int)
dp = np.zeros((5,) + (15,) * 5, int)
dp[(4,) + (0,) * 5] = 1
vis[(4,) + (0,) * 5] = 1
def find(d, a) :
    if vis[(d,) + a] : return dp[(d,) + a]
    ld = (d + 5 - 1) % 5
    rd = (d + 1) % 5
    if a[d] > 0 :
        A = list(a)
        A[d] -= 1
        dp[(d,) + a] += find(ld, tuple(A))
    if (a[rd] > 0) :
        A = list(a)
        A[rd] -= 1
        dp[(d,) + a] += find(rd, tuple(A))
    vis[(d,) + a] = 1
    return dp[(d,) + a]

assert(find(0, (14,) * 5) == 0)
print(find(4, (1, 1, 1, 1, 1)))
print(find(4, (14,) * 5))

# 331951449665644800