import numpy as np
n = 20
m = 9 ** 2 * n
dp = np.zeros((n + 1, m + 1), dtype=int)
s = np.zeros((n + 1, m + 1), int)
dp[0][0] = 1
for i in range(1, n + 1):
    for j in range(0, m + 1):
        for k in range(10):
            if j - k * k >= 0:
                dp[i][j] += dp[i - 1][j - k * k]
                if i >= 12 :
                    s[i][j] += s[i - 1][j - k * k] + dp[i - 1][j - k * k] * k * 10 ** (20 - i)
                    s[i][j] %= 10 ** 9
ans = 0
for i in range(1, 41) :
    ans += s[20][i * i]
    ans %= 10 ** 9
print(ans)
for i in range(21) :
    print(dp[i][1], s[i][1])