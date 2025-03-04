p16 = 2**16
p32 = 2**32
p48 = 2**48
p30 = 2**30
K = 25214903917

d = [0] * 10
# c = [41, 20, 25, 25, 11, 4, 40, 13, 4]
c = [37, 20, 2, 10, 24, 45, 4, 23, 19]
C = [0] * 10
for d[0] in range(0, p16) :
    flag = True
    for i in range(1, 9) :
        d[i] = (K * d[i - 1] + 11) % p16
    for i in range(0, 8) :
        C[i] = (K * c[i] + int((K * d[i] + 11) / p16) - c[i + 1]) % p32
        if C[i] % 4 > 0 :
            flag = False
            break
    if (flag) :
        print(d[0])
        break

k = [0] * 10
for i in range(0, 8):
    C[i] //= 4
for k[0] in range(0, p32 // 52):
    flag = True
    for i in range(1, 9):
        if ((k[i - 1] * K * 13 + C[i - 1]) % p30) % 13 > 0:
            flag = False
            break
        else :
            k[i] = ((k[i - 1] * K * 13 + C[i - 1]) % p30) // 13
    if flag :
        print(k[0])
        break
    if (k[0] % 10000000 == 0): print(k[0])

#k[0] = 42529106, d[0] = 47679
#a[0] = (42529106 * 52 + 41) * 2**16 + 47679 = 144933752257087

#k[i] = 46998144, d[i] = 60091
#a[i] = (46998144 * 52 + 37) * 2**16 + 60091 = 160163661474491