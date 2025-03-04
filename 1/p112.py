def bc(st) :
    a = 0
    b = 0
    for i in range(1, len(st)) :
        if (st[i] < st[i - 1]) : a = 1
        if (st[i] > st[i - 1]) : b = 1
    if (a and b) : return 1
    return 0
    
now = 100
all = 0
while 1 :
    now += 1
    if (bc(str(now))) : all += 1
    # if (all / now >= 0.9) : 
    #     print(now)
    #     exit()
    if (all / now >= 0.99) : 
        print(now)
        exit()