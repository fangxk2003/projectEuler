dp = [[0 for i in range(10)] for j in range(101)]
dp[0][1] = 1
for i in range(1, 101) :
    for j in range(1, 10) :
        for k in range(j, 10) :
            dp[i][k] += dp[i - 1][j]
sum = 0
for y in dp : 
    for x in y : 
        sum += x
sum -= 1
dp = [[0 for i in range(10)] for j in range(101)]
dp[0][9] = 1
for i in range(1, 101) :
    for j in range(0, 10) :
        for k in range(0, j + 1) :
            dp[i][k] += dp[i - 1][j]
    if (i == 1) : dp[i][0] = 0
sum -= 1
for y in dp :
    for x in y : sum += x
sum -= 900
print(sum)