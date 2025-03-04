n = 50
dp = [[[0, 0, 0, 0, 0] for j in range(4)] for i in range(n + 1)]
dp[0][0][0] = 1
for i in range(1, n + 1) :
    dp[i][1][1] = dp[i][2][1] = dp[i][3][1] = dp[i][0][0] = dp[i - 1][0][1] + dp[i - 1][0][0]
    dp[i][1][2] = dp[i - 1][1][1]
    dp[i][2][2] = dp[i - 1][2][1]
    dp[i][2][3] = dp[i - 1][2][2]
    dp[i][3][2] = dp[i - 1][3][1]
    dp[i][3][3] = dp[i - 1][3][2]
    dp[i][3][4] = dp[i - 1][3][3]
    dp[i][0][1] = dp[i][1][2] + dp[i][2][3] + dp[i][3][4]
sum = dp[n][0][1] + dp[n][0][0]
print(sum)