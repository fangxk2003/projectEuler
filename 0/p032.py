def isok(x) :
    vis = [0 for x in range(0, 10)]
    vis[0] = 1
    while(x > 0) :
        if (vis[x % 10]) : return(0)
        vis[x % 10] = 1
        x = x // 10
    return(1)

a = []
for x in range(123456789, 1000000000) :
    if isok(x) :
        # print(x)
        st = str(x)
        for i in range(1, 8) :
            for j in range(i + 1, 9) :
                if (int(st[0 : i]) * int(st[i : j]) == int(st[j : 9])) :
                    if (int(st[j :]) not in a) : a.append(int(st[j :]))
sum = 0
for x in a : sum += x
print(sum)