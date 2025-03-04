def dfs(id, x, y, z, res) :
    if (id == 9) : 
        for i in range(0, 10) : 
            if (not vis[i]) :
                global sum
                sum += res + i * (10 ** id)
                return
    for i in range(0, 10) :
        if (not vis[i]) and (i * 100 + x * 10 + y) % p[id] == 0 :
            vis[i] = 1
            dfs(id + 1, i, x, y, res + i * (10 ** id))
            vis[i] = 0

sum = 0
vis = [0 for i in range(0, 10)]
a = [0 for i in range(0, 10)]
p = [0, 0, 17, 13, 11, 7, 5, 3, 2]
for z in range(0, 10) :
    vis[z] = 1
    for y in range(0, 10) :
        if (vis[y]) : continue
        vis[y] = 1
        dfs(2, y, z, 0, y * 10 + z)
        vis[y] = 0
    vis[z] = 0
print(sum)