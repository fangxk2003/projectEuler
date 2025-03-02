def func(n, d) :
    strn = str(n)
    cnt = 0
    for i in range(len(strn)) :
        if int(strn[i]) == d :
            cnt += int('0' + strn[i+1:]) + 1
        elif int(strn[i]) > d :
            cnt += 10 ** (len(strn) - i - 1)
        cnt += int('0' + strn[:i]) * 10 ** (len(strn) - i - 1)
    return cnt

def find(l, r, d) :
    if l == r : return l
    res = 0
    m = (l + r) // 2
    if (func(m, d) >= l and func(l, d) <= m) :
        res = find(l, m, d)
    if (func(r, d) >= m + 1 and func(m + 1, d) <= r) :
        res += find(m + 1, r, d)
    return res

ans = 0
for i in range(1, 10) :
    ans += find(0, 10 ** 20, i)
print(ans)
# print(func(199981,1))