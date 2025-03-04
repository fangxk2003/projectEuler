n = 50
dp = [[0, 0, 0] for i in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1) :
    dp[i][0] = dp[i - 1][2] + dp[i - 1][0]
    dp[i][1] = dp[i - 1][0] + dp[i - 1][2]
    dp[i][2] = dp[i - 1][1]
sum = dp[n][2] + dp[n][0]

dp = [[0, 0, 0, 0] for i in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1) :
    dp[i][0] = dp[i - 1][3] + dp[i - 1][0]
    dp[i][1] = dp[i - 1][0] + dp[i - 1][3]
    dp[i][2] = dp[i - 1][1]
    dp[i][3] = dp[i - 1][2]
sum += dp[n][3] + dp[n][0]

dp = [[0, 0, 0, 0, 0] for i in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1) :
    dp[i][0] = dp[i - 1][4] + dp[i - 1][0]
    dp[i][1] = dp[i - 1][0] + dp[i - 1][4]
    dp[i][2] = dp[i - 1][1]
    dp[i][3] = dp[i - 1][2]
    dp[i][4] = dp[i - 1][3]
sum += dp[n][4] + dp[n][0]
print(sum - 3)