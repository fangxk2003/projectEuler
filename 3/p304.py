from utils import linear_prime_sieve, matrix_quick_power
import numpy as np
n = 10 ** 14
m = 10 ** 7 + 40
primes, is_prime, phi = linear_prime_sieve(m)
print(primes[-3:])
t = 3500000
pr = [True] * t
pr[0] = False
for p in primes :
    now = (n // p + 1) * p - n
    while now < t : 
        # if p > 10 ** 7 : assert not pr[now]
        pr[now] = False
        now += p
cnt = 0
a = []
for i in range(1, t) :
    if pr[i] : 
        a.append(i)
        cnt += 1
        if cnt == 10 ** 5 : break

# a = []
# now = n
# cnt = 0
# while True : 
#     flag = True
#     for p in primes :
#         if p * p > now : break
#         if now % p == 0 : 
#             flag = False
#             break
#     if flag :
#         a.append(now)
#         cnt += 1
#         if cnt == 10 : break
#     now += 1

print(len(a))
print(a[-1])
fib = np.ones((2, 2), dtype=object)
print(fib.dtype)
fib[1][1] = 0
s = 0
MOD = 1234567891011
# print(matrix_quick_power(fib, 8 - 1, MOD)[0][0])

for val in a :
    # print(val + n - 1)
    s += matrix_quick_power(fib, val + n - 1, MOD)[0][0]
s %= MOD
print(s)

# 389860755200
# 166774221963
# 283988410192
