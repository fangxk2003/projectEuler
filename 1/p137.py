# y = 2
# cnt = 1
# while cnt < 15 :
#     y += 1
#     val = 5 * y ** 2 + 2 * y + 1
#     if (int(val ** 0.5 + 0.5) ** 2 == val) :
#         cnt += 1
#         print(y)
# print(y)

a = [2, 15]
for i in range(2, 15) :
    a.append(a[-1] * 7 - a[-2] + 1)
print(a[-1])
# 1120149658760