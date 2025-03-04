n = 1
while True:
    x = (n + 1) * n // 2
    y = 2
    res = 1
    while y * y <= x:
        now = 1
        while(x % y == 0):
            now += 1
            x /= y
        res *= now
        y += 1
    if (x > 1) : res *= 2
    if (res > 500):
        print((n + 1) * n // 2)
        exit()
    n += 1


