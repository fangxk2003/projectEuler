a = [1]
for i in range(1, 10) : a.append(a[-1] * i)
res = 0
for i in range(3, 100000000) :
    x = i
    sum = 0
    while x > 0 :
        sum += a[x % 10]
        x = x // 10
    if (sum == i) : res += i
print(res)