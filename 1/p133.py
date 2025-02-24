from gmpy2 import next_prime, powmod
n = 10 ** 18
res = 0
p = 5
res = 5
while (p < 10 ** 5) :
    if (powmod(10, n, p) != 1) : res += p
    p = next_prime(p)
print(res)

# 453647705