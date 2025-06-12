# n = 10 ** 9
# p = n * n // 32
# print(p)
# ans = 0
# x = 0
# y = int(p ** 0.5)
# ans = y
# while x * x < p :
#     x += 1
#     while x * x + y * y >= p : y -= 1
#     ans += y
# print(ans)
# ans = ans * 4 + 1 + n * n * 3 // 2 - n // 4 + 1
# print(ans)

from math import sqrt
n = 10 ** 9
p = n * n // 32
print(p)
ans = 0
y = n // 8 - 1
for x in range(n // 8 + 1, int(sqrt(p)) + 1) :
    while x * x + y * y >= p : y -= 1
    ans += y * 2 + 1

ans = ans * 4 + (n // 4 + 1) ** 2 - 4 + n * n * 3 // 2 - n // 4 + 1
print(ans)

# 1598174770424648632
# 1598174770424648488
# 1598174770424648560
# 1598174770174648561
# 1598174770174648498
# 1598174770174689458