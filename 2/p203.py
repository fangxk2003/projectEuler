from utils import linear_prime_sieve
import numpy as np
n = 50
primes, is_prime, phi = linear_prime_sieve(n)
m = len(primes)
s = np.zeros((n + 1, m), int)
for i in range(2, n + 1) :
    v = i
    now = 0
    for j in range(m) :
        s[i][j] = s[i - 1][j]
        while v % primes[j] == 0 :
            v //= primes[j]
            s[i][j] += 1
vis = [False for i in range(2 ** m)]
ans = 0
for i in range(2, n + 1) :
    for j in range(i + 1) :
        p = s[i] - s[j] - s[i - j]
        o = 0
        mul = 1
        for k in range(m) :
            if p[k] > 1 :
                o = -1
                break
            o = o * 2 + p[k]
            if p[k] == 1 : mul *= primes[k]
        if o >= 0 and not vis[o] :
            vis[o] = True
            ans += mul
            # print(mul)
print(ans)
        