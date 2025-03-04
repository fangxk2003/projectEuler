f = [1, 1]
for i in range(1, 31):
    f.append(f[-1] + f[-2])
print(f[-1])