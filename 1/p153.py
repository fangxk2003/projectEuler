# eps = 1e-9
# for x in range(1, 20) :
#     all = []
#     sum = 0
#     for i in range(1, x + 1) :
#         for j in range(-x, x + 1) :
#             a = abs(x * i / (i * i + j * j))
#             b = abs(x * j / (i * i + j * j))
#             if (abs(int(a + 0.5) - a) < eps and abs(int(b + 0.5) - b) < eps) :
#                 all.append((i, j))
#                 sum += i
#     print(x, len(all), sum, all)

def gcd(x, y) :
    if (y == 0) : return(x)
    return gcd(y, x % y)

n = 100000
all = [0 for i in range(n + 1)]
all[1] = 1
for i in range(1, int(n ** 0.5) + 1) :
    for j in range(1, int((n - i * i) ** 0.5) + 1) :
        if (gcd(i, j) == 1) : all[i * i + j * j] += i * 2
ans = 0
for i in range(1, n + 1) :
    if (all[i] > 0) :
        for g in range(1, n // i + 1) : ans += g * all[i] * (n // (g * i))
print(ans)