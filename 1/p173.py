n = 1000000
m = n // 4
ans = 0
for i in range(1, int(m ** 0.5)) :
    ans += m // i - i
print(ans)