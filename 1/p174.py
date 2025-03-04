from utils import factor_count
m = 10 ** 6
t = m // 4
res = [0 for i in range(16)]
for j in range(t + 1) :
    cnt = factor_count(j) // 2
    if cnt > 15 : continue
    res[cnt] += 1
print(res[15])
print(sum(res[1:11]))