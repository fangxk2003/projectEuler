def st(s) :
    return s[1:-1]
myFile = open("C:/Users/Klaus/Desktop/PE/P22/names.txt", 'r')
a = list(map(st, myFile.readline().split(',')))
a.sort()
ans = 0
print(len(a))
for i in range(len(a)) :
    x = 0
    for j in a[i] : x += (ord(j) - ord('A') + 1)
    ans += x * (i + 1)
print(ans)
