res = 0
for x in range(1, 10001) :
    s = 0
    for y in range(1, x) :
        if (x % y == 0) : s += y
    m = 0
    for y in range(1, s) :
        if (s % y == 0) : m += y;
    if m == x and m != s : res += x
print(res)
