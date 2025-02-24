from projeuler import linear_prime_sieve
from collections import Counter
n = 10 ** 7
ans = 0
primes, is_prime, phi = linear_prime_sieve(n)
print(phi[6])
quot_min = n

for i in range(2, n) :
    if Counter(str(i)) == Counter(str(phi[i])) :
        quot = i / phi[i]
        if (quot < quot_min) :
            ans = i
            quot_min = quot
        # print(quot, i)

print(ans)

# 8319823