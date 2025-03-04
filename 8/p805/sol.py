import math 

M = 4
ans = 0
MOD = 1000000007
for u in range(1, M + 1):
    for v in range(1, M + 1):
        X = 10 * v ** 3 - u ** 3
        if math.gcd(u, v) == 1 and X > 0:
            flag = False
            for m in range(1, 1000) :
                p10 = 10 ** m - 1
                p10m = 10 ** (m - 1)
                Y = p10m * u ** 3 - v ** 3
                if (Y >= 0) :
                    for a in range(1, 10) :
                        d = math.gcd(X, a)
                        aa = a // d
                        XX = X // d
                        if p10 % XX == 0 :
                            k = (p10 // XX) * aa
                            if (Y * k) % p10 == 0 :
                                b = (Y * k) // p10
                                if (b < p10m) : 
                                    flag = True
                                    ans += (a * p10m + b) % MOD
                                    print(u, v, m, a)
                                    break
                if flag :
                    break
print(ans % MOD)

