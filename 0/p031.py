ans = 0
for a in range(0, 2) :
    A = 200 - a * 200
    for b in range(0, A // 100 + 1) :
        B = A - b * 100
        for c in range(0, B // 50 + 1) :
            C = B - c * 50
            for d in range(0, C // 20 + 1) :
                D = C - d * 20
                for e in range(0, D // 10 + 1) :
                    E = D - e * 10
                    for f in range(0, E // 5 + 1) :
                        F = E - f * 5
                        for g in range(0, F // 2 + 1) :
                            G = F - g * 2
                            ans += 1
print(ans)