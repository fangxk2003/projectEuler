import math

results = []
def ins(p):
    for i in range(8) :
        if  p[i] == p[0] :
            q = p[i:] + p[:i]
            if (q in results) : return
            q = q[0:1] + q[:0:-1]
            if (q in results) : return
    results.append(p)

for X in range(1, 45 + 1) :
    print(X)
    for Y in range(X, 180 - X) :
        for Z in range(X, 180 - X - Y) :
            if (180 - X - Y - Z < X) : continue
            for W in range(X, Y + 1) :
                x = X / 180 * math.pi
                y = Y / 180 * math.pi
                z = Z / 180 * math.pi
                w = W / 180 * math.pi
                OCdivOD = math.sin(w) / math.sin(x+y-w) * (math.sin(x+y) * math.sin(y+z) / math.sin(x+y+z) / math.sin(y) - 1)
                # print(X, Y, Z, W, OCdivOD)
                Around = 0
                if (abs(OCdivOD - math.cos(x+y)) < 1e-9) : Around = 90
                else :
                    tanA = math.sin(x+y) / (OCdivOD - math.cos(x+y))
                    A = math.atan(tanA) / math.pi * 180
                    if A < 0 : A += 180
                    Around = int(A + 0.5)
                    if (abs(Around - A) > 1e-9) : continue
                if (Around < X) : continue
                if (180 - X - Y - Around < X) : continue
                ins([X, Y, Z, 180 - X - Y - Z, W, X + Y - W, Around, 180 - X - Y - Around])
                
print(len(results))