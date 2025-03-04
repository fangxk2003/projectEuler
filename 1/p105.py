def dfs(id, a, b, sa, sb) :
    # print(id)
    if (id == 0) :
        if (a > 0 and b > 0) :
            if (sa == sb) : return(0)
            if (a > b) :
                if (sa < sb) : return(0)
            if (b > a) :
                if (sb < sa) : return(0)
        return(1)
    global val
    if (not dfs(id - 1, a + 1, b, sa + val[id - 1], sb)) : return(0)
    if (not dfs(id - 1, a, b + 1, sa, sb + val[id - 1])) : return(0)
    if (not dfs(id - 1, a, b, sa, sb)) : return(0)
    return 1

val = []
sum = 0
myFile = open("C:/Users/Klaus/Desktop/PE/P101~150/P105/p105_sets.txt", 'r')
for _ in range(0, 100) :
    val = list(map(int, myFile.readline().split(',')))
    if (dfs(len(val), 0, 0, 0, 0)) :
        for x in val : sum += x
print(sum)