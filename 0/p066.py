from math import gcd
res = 0
sq = 1
for D in range(2, 1001) :
    if (D == (sq + 1) ** 2) :
        sq += 1
        continue
    a, b, c = -sq, 1, 1
    A = [sq]
    while True :
        dnom = b ** 2 * D - a ** 2
        g = gcd(c, dnom)
        c //= g
        dnom //= g
        a, b, c = -a * c, b * c, dnom
        A.append(int((a + b * D ** 0.5) / c))
        a -= A[-1] * c
        if ((a, b, c) == (-sq, 1, 1)) : break
    p = [A[0], A[0] * A[1] + 1]
    q = [1, A[1]]
    for i in range(2, len(A) - 1) :
        p.append(A[i] * p[-1] + p[-2])
        q.append(A[i] * q[-1] + q[-2])
    if (p[-1] ** 2 - D * q[-1] ** 2 != 1) :
        if (p[-1] ** 2 - D * q[-1] ** 2 == -1) :
            p.append(p[-1] ** 2 + D * q[-1] ** 2)
            q.append(p[-1] * q[-1] * 2)
        else :
            print('fail')
            exit()
    if (res < p[-1]) :
        res = p[-1]
        ans = D
print(ans)

# 661