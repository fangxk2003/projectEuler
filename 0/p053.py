import math

def Comp(a, b): return math.factorial(a) / math.factorial(b) / math.factorial(a - b)

ans = 0
for i in range(1, 101):
    for j in range(1, int(i / 2) + 1):
        if Comp(i, j) > 1000000:
            ans += i - j - j + 1
            break
print(ans)