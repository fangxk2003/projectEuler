ans = 0
for l in range(2, 101) :
    for d in range(1, 10) :
        for k in range(1, 10) :
            N = d * (10 ** (l - 1) - k)
            D = 10 * k - 1
            if N % D == 0 :
                m = N // D
                if len(str(m)) == l - 1: 
                    # if l == 2 : print(m, d, k)
                    ans += m % 10000 * 10 + d
ans %= 100000
print(ans)