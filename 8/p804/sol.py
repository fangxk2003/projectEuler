n = 10**16

# y = 0
ans = int(n ** 0.5) * 2

# y > 0, t = 0
ans += int((n // 163)**0.5) * 2

# y > 0, t > 0, even
for y in range(1, int((n // 163)**0.5) + 1):
    m = n - 163 * y * y
    ans += int(m ** 0.5) * 4

#y > 0, t > 0, odd
y = 0
tt = n - 163 * (y * y + y) - 41
while(tt >= 0):
    ans += int((tt + 1/4)**0.5 + 0.5) * 4
    y += 1
    tt = n - 163 * (y * y + y) - 41

print(ans)