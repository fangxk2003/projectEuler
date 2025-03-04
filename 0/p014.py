vis = []
maxR = 0
ans = 0;
for i in range(1, 1000010) : vis.append(0);
for i in range(2, 1000000):
    if (not vis[i]) :
        x = i
        res = 0
        while(x > 1):
            if (x < 1000000 and not vis[x]) : vis[x] = 1
            if (x % 2 == 0) : x = x // 2
            else : x = x * 3 + 1
            res += 1
        if (res > maxR) :
            ans = i;
            maxR = res
print(ans)
