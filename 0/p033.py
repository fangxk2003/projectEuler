def gcd(x, y) :
    if (y == 0) : return(x)
    return gcd(y, x % y)

x = y = 1
for i in range(10, 100) :
    for j in range(i + 1, 100) :
        if (i % 10 == j // 10) :
            if ((i // 10) * j == (j % 10) * i) : 
                x *= i
                y *= j
        if (j % 10 == i // 10) :
            if ((i % 10) * j == (j // 10) * i) :
                x *= i
                y *= j
print(y // gcd(x, y))