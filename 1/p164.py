import numpy as np
dp = np.zeros((20, 10, 10), int)
for i in range(10):
    for j in range(10) :
        if i + j < 10 :
            dp[1][i][j] = 1
for i in range(2, 20) :
    for j in range(10) :
        for k in range(10) :
            if j + k >= 10 : continue
            for l in range(10 - j - k) :
                dp[i][j][k] += dp[i - 1][l][j]
ans = 0
for i in range(1, 10) :
    for j in range(10) :
        ans += dp[19][j][i]
print(ans)