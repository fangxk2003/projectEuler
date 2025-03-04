ss = set()
def slv(x1, y1, x2, y2, x3, y3, x4, y4) :
    if x1 == x2 and x3 == x4 : return
    if x1 == x2 :
        a2 = (y4 - y3) / (x4 - x3)
        b2 = y3 - a2 * x3
        y = a2 * x1 + b2
        if (y - y1) * (y - y2) < 0 :
            if (y - y3) * (y - y4) < 0 :
                x1 = int(x1 * 1000000 + 0.5)
                y = int(y * 1000000 + 0.5)
                ss.add((x1, y))
                return
            if y3 == y4 and (x1 - x3) * (x1 - x4) < 0 :
                x1 = int(x1 * 1000000 + 0.5)
                y = int(y * 1000000 + 0.5)
                ss.add((x1, y))
                return
    else :
        a1 = (y2 - y1) / (x2 - x1)
        b1 = y1 - a1 * x1
        if x3 == x4 :
            y = a1 * x3 + b1
            if (y - y3) * (y - y4) < 0:
                if (y - y1) * (y - y2) < 0 :
                    x3 = int(x3 * 1000000 + 0.5)
                    y = int(y * 1000000 + 0.5)
                    ss.add((x3, y))
                    return
                if y1 == y2 and (x3 - x1) * (x3 - x2) < 0 :
                    x3 = int(x3 * 1000000 + 0.5)
                    y = int(y * 1000000 + 0.5)
                    ss.add((x3, y))
                    return
        else :
            a2 = (y4 - y3) / (x4 - x3)
            b2 = y3 - a2 * x3
            if a1 == a2 : return
            x = (b2 - b1) / (a1 - a2)
            if (x - x1) * (x - x2) < 0 and (x - x3) * (x - x4) < 0 :
                x = int(x * 1000000 + 0.5)
                y = int((a1 * x + b1) * 1000000 + 0.5)
                ss.add((x, y))
                return
    return

cnt = 0
s = [290797]
t = []
n = 5000
for i in range(n * 4) :
    s.append(s[-1] * s[-1] % 50515093)
    t.append(s[-1] % 500)
# print(slv(46, 53, 17, 62, 46, 70, 22, 40))
# input()
for i in range(n) :
    for j in range(i + 1, n) :
        slv(t[i * 4], t[i * 4 + 1], t[i * 4 + 2], t[i * 4 + 3], t[j * 4], t[j * 4 + 1], t[j * 4 + 2], t[j * 4 + 3])
print(len(ss))