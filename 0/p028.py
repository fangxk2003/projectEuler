now = 1
ans = 1
for i in range(1, 501) :
    for j in range(0, 4) :
        now += i * 2
        ans += now
print(ans)