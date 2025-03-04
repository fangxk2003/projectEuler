eps = 1e-12
cnt = 0

def dfs(now, sum, s) :
    global eps, cnt, a, b
    if (abs(sum - 0.5) < eps    ) :
        cnt += 1
        print(cnt, s)
        return
    if (sum > 0.5) : return
    if (now >= len(a)) : return
    dfs(now + 1, sum + 1 / a[now] / a[now], s + [a[now]])
    if (b[-1] - b[now] + sum > 0.5 - eps) : dfs(now + 1, sum, s)

a = [2,3,4,5,6, 7,8,9,10,12, 13,14,15,16,18, 20,21,24,27,28, 30,32,35,36,39, 40,42,45,48,52, 54,56,60,63,64, 65,70,72,80]
b = [0.25]
for i in range(1, len(a)) :
    b.append(b[-1] + 1 / a[i] / a[i])
print(b)
dfs(1, 0.25, [2])
print(cnt)

# https://euler.stephan-brumme.com/152/