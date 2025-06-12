t = 2
while True :
    if (t - 1) / (2 ** t - 2) < 1 / 12345 :
        print(t)
        break
    t += 1
m = 2 ** t - 1
while (t - 1) / (m - 1) < 1 / 12345 :
    m -= 1
m += 1
print(m)
print(m * (m - 1))

# 44043947822