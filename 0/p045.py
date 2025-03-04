import math

def isT(m): return (((8 * m + 1) **0.5 - 1) / 2).is_integer()
def isP(m): return (((24 * m + 1) **0.5 + 1) / 6).is_integer()

i = 10000
while True:
    i += 1
    n = i * (2 * i - 1)
    if isT(n) and isP(n):
        print(n)
        exit()