res = 1
for n in range(2, 10000 + 1) :
    print(n)
    sta = 1
    while True : 
        now = 0
        s = sta
        k = 0
        while s > 0 :
            now += 10 ** k * (s % 3)
            s //= 3
            k += 1
        if now % n == 0 :
            res += now // n
            break
        sta += 1
print(res)

# 1111981904675169