from gmpy2 import next_prime, powmod
p = 5
n = 10 ** 9
res = 0
for i in range(40) :
    while powmod(10, n, p) != 1 :
        p = next_prime(p)
    res += p
    p = next_prime(p)
print(res)

# 843296