# 127035954683
import itertools
from collections import Counter

def find(id, c, now, l) :
    if (id == 5) : 
        return True
    n3 = str(now ** 3)
    while (len(n3) == l) :
        if (Counter(n3) == c) : 
            if (find(id + 1, c, now + 1, l)) : return True
        now += 1
        n3 = str(now ** 3)
    return False

x = 300
while True :
    x3 = str(x ** 3)
    if (find(1, Counter(x3), x + 1, len(x3))) :
        print(x3)
        exit()
    x += 1
    print(x)
