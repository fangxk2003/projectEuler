import numpy as np

pos = np.zeros((2, 36), int)
def find(n, m, p, s): 
    if m == 0 : 
        pos[p][s - 1] += 1
        return
    for i in range(n) :
        find(n, m - 1, p, s + i + 1)

find(4, 9, 0, 0)
find(6, 6, 1, 0)
pre = 0
res = 0
for i in range(36) :
    res += pos[0][i] * pre
    pre += pos[1][i]
print(f"{res / (4 ** 9 * 6 ** 6):.7f}")

# 0.5731441