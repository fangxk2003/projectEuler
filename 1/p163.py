import numpy as np

pt = np.zeros((3997, 6), float)
n = 36
cnt = 0
for i in range(1, n * 2 + 2) :
    for j in range(1, i + 1) :
        if i % 2 == 0 : pt[cnt][0] = np.nan
        else : pt[cnt][0] = (i + 1) // 2
        if (i + j) % 2 == 1 : pt[cnt][1] = np.nan
        else : pt[cnt][1] = (i + j) // 2
        if j % 2 == 0 : pt[cnt][2] = np.nan
        else : pt[cnt][2] = i - (j - 1) // 2
        if j % 2 == 0 : pt[cnt][3] = np.nan
        else : pt[cnt][3] = (j + 1) // 2
        if (i + 1 - j) % 2 == 0 : pt[cnt][4] = np.nan
        else : pt[cnt][4] = (i + 2 - j) // 2
        if i % 2 == 0 : pt[cnt][5] = np.nan
        else : pt[cnt][5] = j - (i + 1) // 2
        cnt += 1
for i in range(1, n + 1) :
    for j in range(1, i + 1) :
        pt[cnt][0] = pt[cnt][3] = pt[cnt][4] = np.nan
        pt[cnt][1] = i + j
        pt[cnt][2] = 2 * i - j + 1
        pt[cnt][5] = 1 - i + (j - 1) * 2
        cnt += 1
for i in range(1, n) :
    for j in range(1, i + 1) :
        pt[cnt][0] = pt[cnt][3] = pt[cnt][4] = np.nan
        pt[cnt][1] = i + j + 1
        pt[cnt][2] = 2 * i - j + 2
        pt[cnt][5] = 1 - i + (j - 1) * 2
        cnt += 1
# print(pt)
print(cnt)
ans = 0
for a in range(cnt) :
    # print(a)
    for b in range(a + 1, cnt) :
        o = -1
        for k in range(6) :
            if pt[a][k] == pt[b][k] and not np.isnan(pt[a][k]) :
                o = k
                break
        if o == -1 : continue
        for c in range(b + 1, cnt) :
            o1 = -1
            for l in range(6) :
                if pt[a][l] == pt[c][l] and not np.isnan(pt[a][l]) :
                    o1 = l
                    break
            if o1 == -1 or o1 == o : continue
            for l in range(6) :
                if l != o and l != o1 and pt[b][l] == pt[c][l] and not np.isnan(pt[b][l]) :
                    ans += 1
                    # print(a, b, c)
                    break
print(ans)