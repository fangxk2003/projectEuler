from gmpy2 import is_prime
now = 2
cnt, res = 0, 0
while True :
    now += 1
    if (now % 2 == 0 or now % 5 == 0 or is_prime(now)) : continue
    s = 1
    sum = 1
    k = 1
    while sum > 0 :
        s = s * 10 % now
        sum = (sum + s) % now
        k += 1
    if ((now - 1) % k == 0) :
        cnt += 1
        res += now
        if (cnt == 25) : break
print(res)

# 149253