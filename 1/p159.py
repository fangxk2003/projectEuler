from utils import prime_factorize
from collections import Counter
res = 0
for i in range(2, 10 ** 6) :
    if (i % 10000 == 0) : print(i)
# for i in range(24, 25) :
    prime_factors = Counter(list(map(lambda x : x % 9, prime_factorize(i))))
    # print(prime_factors)
    res += 3 * (prime_factors[3] // 2)
    if prime_factors[2] <= prime_factors[4] : res += 2 * prime_factors[2]
    else :
        res += 2 * prime_factors[4]
        p2 = prime_factors[2] - prime_factors[4]
        res += 2 * (p2 // 3)
        if p2 % 3 > 0 and prime_factors[3] % 2 > 0 : res += 1
    for j in range(1, 9) :
        res += j * prime_factors[j]
print(res)
"""
    1   2   3   4   5   6   7   8
1   0   0   0   0   0   0   0   0
2       0   1   2   -   -   -   -
3           3   -   -   -   -   -
4               -
"""