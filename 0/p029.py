v = []
for a in range(2, 101) :
    for b in range(2, 101) :
        x = a ** b
        if x not in v : v.append(x)
print(len(v))