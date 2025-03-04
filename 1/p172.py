import numpy as np
m = 4 ** 10
n = 18
dp = np.zeros((n + 1, m), int)
dp[0][0] = 1
ans = 0

def sc(i, j) :
    if dp[i][j] > 0 : return dp[i][j]
    ss = j
    for k in range(10) :
        if ss % 4 > 0 and not(k == 0 and i == 18) : dp[i][j] += sc(i - 1, j - 4 ** k)
        ss //= 4
    return dp[i][j]

for j in range(m) :
    s = 0
    ss = j
    for k in range(10) :
        s += ss % 4
        ss //= 4
        if (s > 18) : break
    if s == 18: ans += sc(18, j)
print(ans)