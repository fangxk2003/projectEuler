from math import gcd
n = 12 * 10 ** 4
is_prime = [True for _ in range(0, n + 1)]
rad = [0 for _ in range(0, n + 1)]
primes = []
rad[1] = 1
for i in range(2, n + 1):
    if is_prime[i]:
        primes.append(i)
        rad[i] = i
    for prime in primes:
        if i * prime > n:
            break
        is_prime[i * prime] = False
        if i % prime == 0:
            rad[i * prime] = rad[i]
            break
        rad[i * prime] = rad[i] * prime

res = 0
for c in range(3, n) :
    x = c // rad[c]
    if (c % 100 == 0) : print(c)
    for a in range(1, (c + 1) // 2) :
        if (rad[a] >= x or rad[c - a] >= x) : continue
        if (gcd(a, c) > 1) : continue
        b = c - a
        if (rad[a] * rad[b] < x) : res += c
print(res)

# 18407904