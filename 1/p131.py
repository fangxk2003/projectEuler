from gmpy2 import is_prime
m, p, cnt = 1, 7, 0
while p < 10 ** 6 :
    if (is_prime(p)) : cnt += 1
    m += 1
    p = 3 * m ** 2 + 3 * m + 1
print(cnt)

# 173