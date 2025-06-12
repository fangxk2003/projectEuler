from math import gcd

s = set()

def rec(p, q, r, a, b, c, n):
    P = a * q * r + b * p * r + c * p * q
    Q = p * q * r
    d = gcd(P, Q)
    P //= d
    Q //= d
    if (P, Q) in s : return
    s.add((P, Q))
    # print(f"({a}/{p}, {b}/{q}, {c}/{r}) ^ {n} -> {P}/{Q}")

for p in range(2, 36) :
    for q in range(2, 36) :
        for r in range(2, 36) :
            if p * q % r == 0 and p * r % q == 0 and q * r % p == 0 :
                for a in range(1, p):
                    if gcd(a, p) > 1 : continue
                    for b in range(1, q):
                        if gcd(b, q) > 1 : continue
                        for c in range(1, r):
                            if gcd(c, r) > 1 : continue
                            x = a * q * r
                            y = b * p * r
                            z = c * p * q
                            if x + y == z : rec(p, q, r, a, b, c, 1)
                            if x ** 2 + y ** 2 == z ** 2 : rec(p, q, r, a, b, c, 2)
for a in range(1, 35) :
    for b in range(1, 35) :
        for c in range(1, 35) :
            if a * b % c == 0 and a * c % b == 0 and b * c % a == 0 :
                for p in range(a + 1, 36) :
                    if gcd(p, a) > 1 : continue
                    for q in range(b + 1, 36) :
                        if gcd(q, b) > 1 : continue
                        for r in range(c + 1, 36) :
                            if gcd(r, c) > 1 : continue
                            x = p * b * c
                            y = q * a * c
                            z = r * a * b
                            if x + y == z : rec(p, q, r, a, b, c, 1)
                            if x ** 2 + y ** 2 == z ** 2 : rec(p, q, r, a, b, c, 2)

u, v = 0, 1
for a, b in s :
    # print(a, b)
    # if (a == 2 and b == 1) : print('---')
    P = a * v + b * u
    Q = b * v
    d = gcd(P, Q)
    P //= d
    Q //= d
    # print(f"{u}/{v} + {a}/{b} = {P}/{Q}")
    u, v = P, Q
print(s)
print(u, v)
print(u + v)

# 27623355790225471
# 409890575807
# !! n can be negative
# 1898841971513533
# 285196020571078987
