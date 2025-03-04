def gfa(x) :
    global fa
    if (fa[x] == x) : return(x)
    fa[x] = gfa(fa[x])
    return fa[x]

e = []
for i in range(1, 41) :
    a = list(map(lambda s : 0 if(s == '-') else int(s), input().split(',')))
    for j in range(0, 40) :
        if (a[j] > 0 and i < j + 1) : e.append((a[j], i, j + 1))
e.sort()
print(e)
fa = [0]
for i in range(1, 41) : fa.append(i)
sum = 0
cnt = 0
for v in e :
    sum += v[0]
    f1 = gfa(v[1])
    f2 = gfa(v[2])
    if f1 != f2 :
        cnt += 1
        fa[f2] = f1
        sum -= v[0]
print(sum)
print(cnt)
