a, c = [0 for _ in range(5)], [0 for _ in range(5)]
f = [True for _ in range(0, 11)]
mst = ''
for s in range(3, 29) :
    for c[0] in range(1, 10) :
        f[c[0]] = False
        for c[1] in range(1, 10) :
            if (not f[c[1]]) : continue
            f[c[1]] = False
            for c[2] in range(1, 10) :
                if (not f[c[2]]) : continue
                f[c[2]] = False
                for c[3] in range(1, 10) :
                    if (not f[c[3]]) : continue
                    f[c[3]] = False
                    for c[4] in range(1, 10) :
                        if (not f[c[4]]) : continue
                        f[c[4]] = False
                        ff = f[:]
                        flag = True
                        for k in range(5) :
                            a[k] = s - c[k] - c[(k + 1) % 5]
                            if (a[k] < 1 or a[k] > 10) :
                                flag = False
                                break
                            if (not ff[a[k]]) :
                                flag = False
                                break
                            ff[a[k]] = False
                        if (not flag) :
                            f[c[4]] = True 
                            continue
                        mini = 10
                        for k in range(5) :
                            st = ''
                            for p in range(5) :
                                st = st + str(a[(k + p) % 5]) + str(c[(k + p) % 5]) + str(c[(k + p + 1) % 5])
                            if (a[k] < mini) : 
                                minst = st
                                mini = a[k]
                        if(minst > mst) : mst = minst
                        f[c[4]] = True
                    f[c[3]] = True
                f[c[2]] = True
            f[c[1]] = True
        f[c[0]] = True
print(mst)
# 6531031914842725