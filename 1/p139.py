from math import gcd
x, y = 0, 1
ans = 0
N = 10 ** 8 - 1
while y < N :
    xx = x + y * 2
    x = y
    y = xx
    xx = x + y * 2
    x = y
    y = xx
    k = y ** 2
    u = k + int((2 * k - 1) ** 0.5 + 0.5)
    d = k - 1
    g = gcd(u, d)
    u //= g
    d //= g
    ans += N // ((y + 1) * u - (y - 1) * d)
print(ans)

# 10057761