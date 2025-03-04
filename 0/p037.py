def isP(x) :
    if (x < 2) : return(0)
    for i in range(2, int(x ** 0.5) + 1) :
        if x % i == 0 : return(0)
    return(1)

sum = 0
cnt = 0
for i in range(11, 100000000) :
    x = i
    ok = 1
    while x > 0:
        if (not isP(x)) :
            ok = 0
            break
        x = x // 10
    x = i
    if (not ok) : continue
    while x > 0:
        if (not isP(x)) :
            ok = 0
            break
        if (x >= 10) : x = int(str(x)[1 :])
        else : x = 0
    if (ok) :
        cnt += 1
        sum += i
        if (cnt == 11) :
            print(sum)
            exit()

