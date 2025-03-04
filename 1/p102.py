def S(x, y, z) :
    return abs((y[0] - x[0]) * (z[1] - x[1]) - (y[1] - x[1]) * (z[0] - x[0]))

myFile = open("C:/Users/Klaus/Desktop/PE/P101~150/P102/p102_triangles.txt", 'r')
O = (0, 0)
cnt = 0
for _ in range(0, 1000) :
    a = list(map(int, myFile.readline().split(',')))
    b = [(a[0], a[1]), (a[2], a[3]), (a[4], a[5])]
    if (S(b[0], b[1], O) + S(b[1], b[2], O) + S(b[2], b[0], O) == S(b[0], b[1], b[2])) :
        cnt += 1
print(cnt)