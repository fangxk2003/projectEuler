import numpy as np

n = 10 ** 18 + 1
pow2 = 1
k = 0
M = 10 ** 9
while pow2 * 2 <= n :
    k += 1
    pow2 *= 2
pt1 = 2 * (2 ** (k - 2) - 1) * (2 ** k - 1) * (2 ** (k - 1) - 1) % M
print(pt1)
rm = n - pow2
assert rm % 2 == 1
t = rm // 2
pt2 = ((2 * t - 1) * (2 ** k - 1 + t) * (2 * t + 1) + 2 ** k - 1 + 2 * t) % M
print(pt2)
t -= 1
pow2 = 1
k = 0
pt3 = 0
while pow2 <= t :
    now = 0
    if t & pow2 : now = t % pow2 + 1
    now += (t - t % (pow2 * 2)) // 2
    pt3 += now * (2 ** (k + 1) + 2 ** (k + 2) - 3) * 2 ** (k + 1)
    pow2 *= 2
    k += 1
t += 1
pow2 = 1
k = 0
while pow2 <= t :
    if t & pow2 : pt3 += (2 ** (k + 1) + 2 ** (k + 2) - 3) * 2 ** k
    pow2 *= 2
    k += 1
pt3 %= M
print(pt3)
ans = (pt1 + pt2 + pt3) % M
print(ans)

# m = 16
# vis = np.zeros((m, m), int)
# for n in range(10, 11) :
#     ans = 0
#     los = np.ones((n, n, n), int)
#     for a in range(n) :
#         for b in range(a + 1, n) :
#             for c in range(b + 1, n) :
#                 if los[a][b][c] == 1 :
#                     if a > 0 :
#                         vis[n][a] += 1
#                         vis[n][b] += 1
#                         vis[n][c] += 1
#                         # print(a, b, c)
#                         ans += a + b + c
#                     for k in range(c + 1, n) : los[a][b][k] = 0
#                     for k in range(b + 1, n) :
#                         if k < c : los[a][k][c] = 0
#                         if k > c : los[a][c][k] = 0
#                     for k in range(a + 1, n) :
#                         if k < b : los[k][b][c] = 0
#                         if k > b and k < c : los[b][k][c] = 0
#                         if k > c : los[b][c][k] = 0
#     res = 0
#     for i in range(n) :
#         res += vis[n][i] * i
#     print(res)
#     print(vis[n])
# for n in range(m - 1, 0, -1) :
#     vis[n] -= vis[n - 1]
# for i in range(m):
#     for x in vis[i]: print(x, end=' ')
#     print(i + 1)
# 2 6 14 30 62