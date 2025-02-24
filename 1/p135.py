res = 0
for v in range(1155, 10 ** 6) :
    cnt = 0
    if (int(v ** 0.5 + 0.5) ** 2 == v) :
        if (v % 4 == 0) : cnt = 1
    n = 1
    while (n ** 2 < v) :
        if (v % n == 0) :
            p = v // n
            if (n + p) % 4 == 0 :
                d = (n + p) // 4
                if (d < n) : cnt += 1
                if (d < p) : cnt += 1
        n += 1
    if cnt == 10 : 
        res += 1
        # print(res)
print(res)

# 4989
