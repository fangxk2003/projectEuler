import math

val = [32, 32, 32, 34, 36, 34]
sum = [0]
pre9 = [0, 5, 1, 6, 2, 7, 3, 8, 4]

for r in range(0, 5) :
    sum.append(sum[-1] + val[r])

ans = 0
L = 10 ** 18
for r in range(0, 6) :
    print(r)
    K = (L - r) // 6
    c1 = 2 ** (r + 1)
    c2 = 200 - 2 ** 5 - 54 - sum[r]
    b = pre9[(c1 + c2) % 9]
    T = (K - b) // 9
    c1 *= 64 ** b
    c2 -= 200 * b
    rec = 1216562
    p = 1997 * 4877
    p0 = 9688229
    ans += (T // (p * rec)) * rec
    T %= (p * rec)
    pp0 = 1
    for mo in range(0, rec) :
        no = (c1 * pp0 + c2 - mo * 1800) * 7338443 % p
        if no * rec + mo <= T : ans += 1
        pp0 = pp0 * p0 % p
print(ans)



# import math

# val = [32, 32, 32, 34, 36, 34]
# sum = [0]
# pre9 = [0, 5, 1, 6, 2, 7, 3, 8, 4]

# for r in range(0, 5) :
#     sum.append(sum[-1] + val[r])

# ans = 0
# L = 5 * 10 ** 9
# for r in range(0, 6) :
#     print(r)
#     K = (L - r) // 6
#     c1 = 2 ** (r + 1)
#     c2 = 200 - 2 ** 5 - 54 - sum[r]
#     b = pre9[(c1 + c2) % 9]
#     T = (K - b) // 9
#     c1 *= 64 ** b
#     c2 -= 200 * b
#     p = 1997 * 1996
#     cnt = 0
#     p782 = 1
#     C1 = c1 % 1997
#     C2 = c2 % 1997
#     vis = [0] * 1997
#     for t in range(0, p):
#         if (C1 * p782 + 197 * t + C2) % 1997 == 0 :
#             cnt += 1
#             if vis[t // 1996] == 0 : vis[t // 1996] = 1
#             else : print("*")
#         p782 = p782 * 782 % 1997
#     print(cnt)
#     exit()
#     ans += cnt * (T // p)
#     p782 = 1
#     for t in range(1, T % p + 1) :
#         if (C1 * p782 + 197 * t + C2) % 1997 == 0 : ans += 1
#         p782 = p782 * 782 % 1997
#     C1 = c1 % 4877
#     C2 = c2 % 4877
#     p = 4877 * 4876
#     cnt = 0
#     p2507 = 1
#     for t in range(0, p):
#         if (C1 * p2507 + 3077 * t + C2) % 4877 == 0 : cnt += 1
#         p2507 = p2507 * 2507 % 4877
#     print(cnt)
#     ans += cnt * (T // p)
#     p2507 = 1
#     for t in range(1, T % p + 1) :
#         if (C1 * p2507 + 3077 * t + C2) % 4877 == 0 : ans += 1
#         p2507 = p2507 * 2507 % 4877
# print(ans)