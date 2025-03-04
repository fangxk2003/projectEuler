ans = 0
for i in range(2, 1000000) :
    x = i
    all = 0
    while x > 0 :
        all += (x % 10) ** 5
        x = x // 10
    if all == i : ans += i
print(ans)