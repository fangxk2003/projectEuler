d = 1
N = 5 * 10 ** 7
c = [0 for _ in range(N)]
while d * 4 - 1 < N :
    for n in range(d + 1, 2 * d) :
        v = (d * 4 - n) * n
        if (v >= N) : break
        c[v] += 2
    if 4 * d ** 2 < N : c[4 * d ** 2] += 1
    for n in range(1, d + 1) :
        v = (d * 4 - n) * n 
        if (v >= N) : break
        c[v] += 1
    d += 1
    # if (d % 10000 == 0) : print(d)

res = 0
for i in range(N) :
    if (c[i] == 1) : res += 1
print(res)

# 2544559