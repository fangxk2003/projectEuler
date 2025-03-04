s = []
d = []
t = []
for i in range(1, 21) : s.append(i)
s.append(25)
for i in range(1, 21) : d.append(i * 2)
d.append(50)
for i in range(1, 21) : t.append(i * 3)
all = s + d + t
ans = 21
for i in range(21) :
    for j in range(62) :
        if (all[j] + d[i] < 100) : ans += 1
        for k in range(j, 62) :
            if all[j] + all[k] + d[i] < 100 : ans += 1
print(ans)
