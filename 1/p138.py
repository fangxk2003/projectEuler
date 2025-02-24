a, b = 0, 1
res = 0
for i in range(12) :
    aa = a + b * 4
    a = b
    b = aa
    aa = a + b * 4
    a = b
    b = aa
    res += b
    print(b)
print(res)

# 1118049290473932