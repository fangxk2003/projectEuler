from gmpy2 import is_prime
mp = {}
mp[0, 0] = 1
N = 10000000
l = 2
p = 0
d = 1
x, y = 0, 1
id = {}
id[1] = (0, 0)
for i in range(2, N + 1) :
    mp[x, y] = i
    id[i] = (x, y)
    if p == 0 :
        x -= 1
    elif p == 1 :
        y -= 1
    elif p == 2 :
        x += 1
        y -= 1
    elif p == 3 :
        x += 1
    elif p == 4 :
        y += 1
    elif p == 5 :
        x -= 1
        y += 1
    d += 1
    if (d == l) : 
        if (p == 5) :
            p = 0
            l += 1
            y += 1
            d = 1
        else :
            p += 1
            d = 1

now = 1
cnt = 0
while cnt < 2000 :
    cor = id[now]
    o = 0
    for i in [[0, 1], [-1, 1], [-1, 0], [0, -1], [1, -1], [1, 0]] :
        x, y = cor[0] + i[0], cor[1] + i[1]
        if (is_prime(abs(mp[x, y] - mp[cor]))) : o += 1
    if (o == 3) : 
        cnt += 1
        print(cnt, now)
    now += 1
print(now - 1)