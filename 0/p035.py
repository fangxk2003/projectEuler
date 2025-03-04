def isP(x) :
    for i in range(2, int(x ** 0.5) + 1) :
        if x % i == 0 : return(0)
    return(1)
ans = 4
for i in range(10, 1000000) :
    if (isP(i)) :
        ok = 1
        x = int(str(i % 10) + str(i // 10))
        while(x != i) :
            if (not isP(x)) :
                ok = 0
                break
            x = int(str(x % 10) + str(x // 10))
        ans += ok
print(ans)
