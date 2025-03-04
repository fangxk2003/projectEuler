from utils import linear_prime_sieve
n = 100
m = 10 ** 9
primes, is_prime, phi = linear_prime_sieve(n)
s = set()
s.add(1)
for p in primes :
    ss = set()
    for x in s :
        y = x
        while y <= m :
            ss.add(y)
            y *= p
    s = ss
    # print(s)
print(len(s))
