k = 10 ** 25
bi = []
while k > 0 :
    bi.append(k % 2)
    k = k // 2
bi.reverse()
dp = [[0, 0] for i in range(len(bi))]
dp[0][0] = 1
dp[0][1] = 1
for i in range(1, len(bi)) :
    if bi[i] == 0 :
        dp[i][0] = dp[i - 1][1] + dp[i - 1][0]
        dp[i][1] = dp[i - 1][1]
    else :
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = dp[i - 1][0] + dp[i - 1][1]
print(dp[len(bi) - 1][0])