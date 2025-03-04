p = 9688229
MOD = 1997 * 4877
now = p * p % MOD
cnt = 2
while (now != p) :
    now = now * p % MOD
    cnt += 1
print(now, cnt)