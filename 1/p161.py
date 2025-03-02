import numpy as np
n = 9
m = 12
dp = np.zeros((m + 1, 3 ** n), int)

def sc(c, val, l, now) :
    # print(c, val, l, now)
    if now == n :
        new_sta = 0
        for i in range(n) :
            new_sta = new_sta * 3 + c[i] - 1
        # if l == 2 and new_sta == 4 :
        #     print('--')
        dp[l][new_sta] += val
        return
    '''
    #
    #
    #
    '''
    c[now] = 3
    nxt = now + 1
    while nxt < n and c[nxt] > 0 : nxt += 1
    sc(c, val, l, nxt)
    c[now] = 0
    '''
     #
    ##
    '''
    if now > 0 and c[now - 1] == 1 :
        c[now - 1] = 2
        c[now] = 2
        nxt = now + 1
        while nxt < n and c[nxt] > 0 : nxt += 1
        sc(c, val, l, nxt)
        c[now - 1] = 1
        c[now] = 0
    '''
    #
    ##
    '''
    if now < n - 1 and c[now + 1] == 1 :
        c[now] = 2
        c[now + 1] = 2
        nxt = now + 2
        while nxt < n and c[nxt] > 0 : nxt += 1
        sc(c, val, l, nxt)
        c[now] = 0
        c[now + 1] = 1
    '''
    ##
    #
    '''
    if now < n - 1 and c[now + 1] == 0 :
        c[now] = 2
        c[now + 1] = 1
        nxt = now + 2
        while nxt < n and c[nxt] > 0 : nxt += 1
        sc(c, val, l, nxt)
        c[now] = 0
        c[now + 1] = 0
    '''
    ##
     #
    '''
    if now < n - 1 and c[now + 1] == 0 :
        c[now] = 1
        c[now + 1] = 2
        nxt = now + 2
        while nxt < n and c[nxt] > 0 : nxt += 1
        sc(c, val, l, nxt)
        c[now] = 0
        c[now + 1] = 0
    '''
    ###
    '''
    if now < n - 2 and c[now + 1] == 0 and c[now + 2] == 0 :
        c[now] = 1
        c[now + 1] = 1
        c[now + 2] = 1
        nxt = now + 3
        while nxt < n and c[nxt] > 0 : nxt += 1
        sc(c, val, l, nxt)
        c[now] = 0
        c[now + 1] = 0
        c[now + 2] = 0
    '''
    #&&
    ##&
    '''
    if now < n - 2 and c[now + 1] == 0 and c[now + 2] == 0 :
        c[now] = 2
        c[now + 1] = 2
        c[now + 2] = 2
        nxt = now + 3
        while nxt < n and c[nxt] > 0 : nxt += 1
        sc(c, val, l, nxt)
        c[now] = 0
        c[now + 1] = 0
        c[now + 2] = 0
    '''
    #&&&
    ##
    '''
    if now < n - 3 and c[now + 1] == 0 and c[now + 2] == 0 and c[now + 3] == 0 :
        c[now] = 2
        c[now + 1] = 2
        c[now + 2] = 1
        c[now + 3] = 1
        nxt = now + 4
        while nxt < n and c[nxt] > 0 : nxt += 1
        sc(c, val, l, nxt)
        c[now] = 0
        c[now + 1] = 0
        c[now + 2] = 0
        c[now + 3] = 0

dp[0][0] = 1
for i in range(m) :
    for sta in range(3 ** n) :
        if dp[i][sta] == 0 : continue
        ss = sta
        c = [0] * n
        for j in range(n) :
            c[j] = ss % 3
            ss //= 3
        now = 0
        while now < n and c[now] > 0 : now += 1
        # print(dp[i][sta], i, sta)
        sc(c, dp[i][sta], i + 1, now)
print(dp[m][0])
# print(dp)