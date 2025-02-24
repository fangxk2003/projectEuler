from math import gcd
sq = 1
ans = 0
for i in range(2, 10001) :
    if (i == (sq + 1) ** 2) : 
        sq += 1
        continue
    a, b, c = -sq, 1, 1
    cnt = 0
    while True :
        cnt += 1
        dnom = b ** 2 * i - a ** 2
        # print('d', dnom)
        g = gcd(c, dnom)
        # print('g=', g)
        c //= g
        dnom //= g
        a, b, c = -a * c, b * c, dnom
        a -= int((a + b * i ** 0.5) / c) * c
        # print(a, b, c)
        if ((a, b, c) == (-sq, 1, 1)) : break
    if (cnt % 2 == 1) : ans += 1
print(ans)

 # 1322