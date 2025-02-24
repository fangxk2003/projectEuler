from gmpy2 import next_prime, powmod

p1 = 5
res = 0
while p1 < 10 ** 6 :
    p2 = next_prime(p1)
    bs = 10 ** len(str(p1))
    ans = (p2 - p1) * powmod(bs, p2 - 2, p2) % p2 * bs + p1
    res += ans
    # print(ans, p1, p2)
    p1 = p2
print(res)
# 18613426663617118