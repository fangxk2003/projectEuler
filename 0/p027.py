maxn = 0
co = 0

def isP(x) :
    if (x < 2) : return 0
    for i in range(2, int(x ** 0.5) + 1) :
        if x % i == 0 : return(0)
    return(1)

for a in range(-999, 1000) : 
    for b in range(2, 1001) :
        n = 0
        while isP(n * n + a * n + b) : n += 1
        if (n > maxn) :
            maxn = n
            co = a * b
print(co)

            

