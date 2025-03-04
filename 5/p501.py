from utils import n34_prime_sieve_count as mpcon
from utils import linear_prime_sieve
N = 10 ** 12
S = mpcon(N)
print('1e12done')
m = 10 ** 6
primes, is_prime, phi = linear_prime_sieve(m)
print('1e6done')
ans = S[int(N ** (1/7))]
i = 0
while primes[i] ** 3 <= N :
    print(i)
    ans += S[N // primes[i] ** 3]
    i += 1
ans -= S[int(N ** (1/4))]
i = 0
while primes[i] ** 3 <= N :
    print(i)
    j = i + 1
    while primes[j] < (N / primes[i]) ** 0.5 :
        # print(j)
        ans += S[N // primes[i] // primes[j]] - S[primes[j]]
        j += 1
    i += 1
print(ans)
