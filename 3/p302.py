from utils import linear_prime_sieve
from math import gcd
import sys
import time
sys.setrecursionlimit(80000)
n = 10 ** 18
m = 10 ** 6
primes, is_prime, phi = linear_prime_sieve(m)

res = 0

def srch(id, n, d, lft, phi_d):
    if id == -1: 
        assert lft == 1
        assert d > 0
        assert phi_d > 0
        if d == 1 and phi_d == 1 :
            global res
            res += 1
        return
    cnt = 0
    while lft % primes[id] == 0:
        lft //= primes[id]
        cnt += 1
    if cnt != 1 : srch(id - 1, n, d, lft, gcd(phi_d, cnt))
    pow = 2
    while primes[id] ** pow <= n:
        phi_d_now = pow - 1 + cnt
        if phi_d_now == 1 : 
            pow += 1
            continue
        srch(id - 1, n // (primes[id] ** pow), gcd(d, pow), lft * (primes[id] - 1), gcd(phi_d, phi_d_now))
        pow += 1

print(len(primes))
start_time = time.time()

for p in range(1, 52000):
    if (p % 1000 == 0) : 
        print(f"Time taken for p={p}: {time.time() - start_time:.2f} seconds")
        print(p)
        start_time = time.time()
        print(res)
    pow = 3
    while primes[p] ** pow <= n :
        srch(p - 1, n // (primes[p] ** pow), pow, primes[p] - 1, pow - 1)
        pow += 1
print(res)

# 1116887
# 1170060