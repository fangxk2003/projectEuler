def func(a, b, c, n) :
    return a * b + b * c + c * a + 2 * (n - 1) * (a + b + c)

N = 154
while True :
    n = 1
    cnt = 0
    while (4 * n ** 2 + 2 <= N) :
        M = (N - 4 * (n - 1) * (n - 2)) // 2
        a = 1
        while (func(a, a, a, n) <= M) :
            b = a
            while (func(a, b, b, n) <= M) :
                c = (M - a * b - 2 * (n - 1) * (a + b)) / (a + b + 2 * (n - 1))
                if (abs(int(c + 0.5) - c) < 0.00001) : cnt += 1
                b += 1
            a += 1
        n += 1
    if (cnt == 1000) :
        print(N)
        exit()
    N += 1
    if (N % 100 == 0) : print(N)
# 18522