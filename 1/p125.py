s = [0]
n, m = 10 ** 4, 10 ** 8
for i in range(1, n + 1) :
    s.append(s[-1] + i ** 2)

ans = []
for x in range(0, n) :
    for y in range(x + 2, n + 1) :
        val = s[y] - s[x]
        if (val >= m) : continue
        if (str(val)[::-1] == str(val)) : 
            ans.append(val)
print(sum(set(ans)))
# 2906969179