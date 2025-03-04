a = []
for i in range(0, 100):
    b = list(map(int, input().split()))
    a.append(b)
dp = a
for i in range(1, 100):
    dp[i][0] += dp[i - 1][0]
    dp[i][i] += dp[i - 1][i - 1]
    for j in range(1, i):
        dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])
ans = 0
for i in range(0, 100) :
    ans = max(ans, dp[99][i])
print(ans)
