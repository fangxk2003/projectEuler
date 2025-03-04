dp=[[1 for x in range(0, 21)] for y in range(0, 21)]
dp[0][0] = 1;
for i in range(1, 21):
    for j in range(1, 21): dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
print(dp[20][20])