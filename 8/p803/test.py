a = [160163661474491]
for i in range(1, 100):
    a.append((a[-1] * 25214903917 + 11) % (2 ** 48))
b = []
c = []
for i in range(0, 100):
    b.append(int(a[i] / (2 ** 16)) % 52)
    if b[-1] > 25 :
        c.append(chr(ord('A') + b[-1] - 26))
    else :
        c.append(chr(ord('a') + b[-1]))
print(c)