now = 1
st = ''
while len(st) < 1000000 :
    st = st + str(now)
    now += 1
ans = 1
for i in range(0, 7) :
    ans *= int(st[10 ** i - 1])
print(ans)