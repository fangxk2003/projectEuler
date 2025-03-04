a = []
ans = 0
for n in range(1, 11) :
    x = 0
    for i in range(0, 11) :
        x += (-n) ** i
    a.append(x)
    print(x)
    res = 0
    for i in range(0, n) :
        now = a[i]
        for k in range(0, n) :
            if (i == k) : continue
            now *= (n - k) / (i - k)
        res += now
    ans += res
print(ans)