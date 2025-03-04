p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
res = 100000000000000000000000000000 
a = [0 for i in range(14)]
for a[0] in range(1, 10) :
    for a[1] in range(1, 8) :
        for a[2] in range(1, 7) :
            for a[3] in range(1, 5) :
                for a[4] in range(1, 4) :
                    for a[5] in range(1, 3) :
                        for a[6] in range(1, 2) :
                            now = 1
                            ans = 1
                            for i in range(0, 7) :
                                now *= (1 + a[i] * 2)
                                ans *= p[i] ** a[i]
                            for i in range(7, 14) :
                                if (now > 8000001) :
                                    res = min(res, ans)
                                    break
                                now *= 3
                                ans *= p[i]
print(res)