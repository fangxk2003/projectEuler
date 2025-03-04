maxi = 0
maxx = 0
for i in range(1, 1001) :
    cnt = 0
    for j in range(1, i) :
        a2pb2 = j ** 2
        apb = i - j
        ab = apb ** 2 - a2pb2
        if ab <= 0 or ab % 2 == 1 :
            continue
        amb2 = a2pb2 - ab
        if (amb2 < 0 or int(amb2 ** 0.5) ** 2 != amb2) :
            continue
        amb = int(amb2 ** 0.5)
        a2 = apb + amb
        b2 = apb - amb
        if a2 % 2 == 1 or b2 % 2 == 1 or a2 <= 0 or b2 <= 0 :
            continue
        cnt += 1
    if cnt > maxx :
        maxx = cnt
        maxi = i
print(maxi)
