def isP(x) :
    for i in range(2, int(x ** 0.5) + 1) :
        if (x % i == 0) : return(0)
    return(1)

sum = 0
for a in range(1, 10) :
    for b in range(1, 10) :
        if (isP(a * (10 ** 9) + b)) :
            sum += a * (10 ** 9) + b
print(sum)
for i in range(1, 10) :
    cnt = 0
    for j in range(0, 10) :
        for k in range(0, 10) :
            if (i == k) : continue
            x = 1111111111 * i - (i - k) * (10 ** j)
            if (x < 10 ** 9) : continue
            if (isP(x)) :
                cnt += 1
                sum += x
    if (cnt == 0) :
        for j1 in range(0, 10) :
            for j2 in range(j1 + 1, 10) :
                for k1 in range(0, 10) :
                    for k2 in range(0, 10) :
                        x = 1111111111 * i - (i - k1) * (10 ** j1) - (i - k2) * (10 ** j2)
                        if (x < 10 ** 9) : continue
                        if (isP(x)) :
                            cnt += 1
                            sum += x
        print(cnt)
    else : print(cnt)
print(sum)
