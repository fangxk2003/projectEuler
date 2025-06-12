from utils import linear_prime_sieve, prime_factorize
from collections import Counter

n = 10**7
_, _, _, num_div = linear_prime_sieve(n, True)

res = 0
for i in range(3, n) :
    if num_div[i] == num_div[i - 1] : res += 1
print(res)