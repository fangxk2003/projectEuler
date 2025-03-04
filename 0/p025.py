a = [0, 1]
while 1 :
    a.append(a[-2] + a[-1])
    if (len(str(a[-1])) >= 1000) : 
        print(len(a) - 1)
        exit()