res = 0
ans = 0
for i in range(2, 1000) :
    a = [0 for x in range(0, i)]
    now = 1
    k = 1
    while 1 :
        now = now * 10 % i
        if a[now] > 0 :
            if (k - a[now] > ans) :
                ans = k - a[now]
                res = i
            break
        else : a[now] = k
        k += 1
print(res)