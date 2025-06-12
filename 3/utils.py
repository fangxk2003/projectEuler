import numpy as np
def linear_prime_sieve(n, is_num_divisors = False) :
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    phi = [0] * (n + 1)
    num_div = [0] * (n + 1) if is_num_divisors else None
    phi[1] = 1
    if is_num_divisors : num_div[1] = 1
    for i in range(2, n + 1):
        if is_prime[i] :
            if is_num_divisors : num_div[i] = 2
            phi[i] = i - 1
            primes.append(i)
        for prime in primes:
            if prime * i > n : break
            is_prime[prime * i] = False
            if i % prime == 0 :
                if is_num_divisors :
                    ii = i
                    while ii % prime == 0 : ii //= prime
                    num_div[prime * i] = num_div[i] + num_div[ii]
                phi[prime * i] = phi[i] * prime
                break
            else : 
                if is_num_divisors : num_div[prime * i] = num_div[i] * 2
                phi[prime * i] = phi[i] * (prime - 1)
    if is_num_divisors : return primes, is_prime, phi, num_div
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
    res = np.zeros((pd, pd), dtype=object)
    for i in range(pd) : res[i][i] = 1
    while n > 0 :
        if n & 1 : res = res @ mat
        for i in range(pd) :
            for j in range(pd) :
                res[i][j] %= mod
        mat = mat @ mat
        for i in range(pd) :
            for j in range(pd) :
                mat[i][j] %= mod
        n >>= 1
    return res