import numpy as np
def linear_prime_sieve(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    phi = [0] * (n + 1)
    phi[1] = 1
    for i in range(2, n + 1):
        if is_prime[i] :
            phi[i] = i - 1
            primes.append(i)
        for prime in primes:
            if prime * i > n : break
            is_prime[prime * i] = False
            if i % prime == 0 :
                phi[prime * i] = phi[i] * prime
                break
            else : phi[prime * i] = phi[i] * (prime - 1)
    return primes, is_prime, phi

def factor_count(n) :
    count = 0
    for i in range(1, int(n ** 0.5) + 1) :
        if n % i == 0 :
            count += 1
            if i != n // i : count += 1
    return count

def prime_factorize(n) :
    factors = []
    for i in range(2, int(n ** 0.5) + 1) :
        while n % i == 0 :
            factors.append(i)
            n //= i
    if n != 1 : factors.append(n)
    return factors

def quick_power(x, y, mod) :
    res = 1
    while y > 0 :
        if y & 1 : res = res * x % mod
        x = x * x % mod
        y >>= 1
    return res

def matrix_quick_power(mat, n, mod) :
    pd = len(mat)
    res = np.zeros((pd, pd), int)
    for i in range(pd) : res[i][i] = 1
    while n > 0 :
        if n & 1 : res = res @ mat % mod
        mat = mat @ mat % mod
        n >>= 1
    return res

def n34_prime_sieve_sum(n) :
    r = int(n ** 0.5)
    V = [n // i for i in range(1, r + 1)]
    V += list(range(V[-1] - 1, 0, -1))
    S = {i:i * (i + 1) // 2 - 1 for i in V}
    for p in range(2, r + 1):
        if S[p] > S[p - 1]:  # p is prime
            sp = S[p - 1]  # sum of primes smaller than p
            p2 = p * p
            for v in V:
                if v < p2: break
                S[v] -= p * (S[v // p] - sp)
    return S[n]

def n34_prime_sieve_count(n) :
    r = int(n ** 0.5)
    V = [n // i for i in range(1, r + 1)]
    V += list(range(V[-1] - 1, 0, -1))
    S = {i:i - 1 for i in V}
    for p in range(2, r + 1):
        if S[p] > S[p - 1]:
            sp = S[p - 1]
            p2 = p * p
            for v in V:
                if v < p2: break
                S[v] -= S[v // p] - sp
    return S

def gcd(x, y) :
    while y:
        x, y = y, x % y
    return x