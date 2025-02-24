now = 10 ** 6

while True :
    now += 1
    if (now % 2 == 0 or now % 5 == 0) : continue
    s = 1
    sum = 1
    k = 1
    while sum > 0 :
        s = s * 10 % now
        sum = (sum + s) % now
        k += 1
    if (k > 10 ** 6) :
        print(now)
        exit()

# 1000023