p16 = 2**16
p32 = 2**32
p48 = 2**48
p30 = 2**30
K = 25214903917
d = 47679
dd = 60091
a = 144933752257087
aa = 160163661474491

ans = 0
while d != dd:
    d = (K * d + 11) % p16
    a = (K * a + 11) % p48
    ans += 1

A = 1
B = 0
for i in range(0, p16):
    B += A
    A *= K
    A %= p48
B = B * 11 % p48
cnt = 0
while(a != aa):
    cnt += 1
    if (cnt % 10000000 == 0) : print(cnt)
    a = (A * a + B) % p48
print(cnt)
ans = ans + cnt * p16
print(ans)