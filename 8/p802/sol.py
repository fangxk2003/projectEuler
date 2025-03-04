n = 10**7-1
p = 2
res = 1
MOD = 1020340567

while(n > 0) :
    if (n & 1) :
        res = res * p % MOD
    p = p * p % MOD
    n = int(n / 2)
print(res)