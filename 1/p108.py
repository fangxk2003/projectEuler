eps = 1e-9
for n in range(4, 1000000) :
    k = 2
    cnt = 1
    m = n
    while k * k <= m :
        now = 1
        while (m % k == 0) :
            m = m // k
            now += 2
        cnt *= now
        k += 1
    if (m > 1) : cnt *= 3
    cnt = (cnt + 1) // 2
    if (cnt > 1000) : 
        print(n)
        exit()
