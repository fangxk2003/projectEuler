def year(x) :
    return x % 4 == 0 and x % 100 != 0 or x % 400 == 0

a = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d = 1
for i in range(1, 13) : d += a[i]
ans = 0
for i in range(1901, 2001) :
    a[2] += year(i)
    for j in range(1, 13) : 
        if (d % 7 == 0) : ans += 1
        d += a[j]
    a[2] -= year(i)
print(ans)