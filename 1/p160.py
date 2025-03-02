from utils import quick_power
M = 10 ** 5
tl = [1]
num = [0, 1, 1, 2, 2, 2, 2, 3, 3, 4]
for i in range(1, 10 ** 5) :
    if i % 2 == 0 or i % 5 == 0 :
        tl.append(tl[-1])
    else :
        tl.append(tl[-1] * i % M)
res = 1
cnt2 = 0
a2 = 1
N = 10 ** 12
all2 = 0
while a2 <= N :
    val = a2
    cnt5 = 0
    while val <= N:
        n = N // val
        now = quick_power(tl[-1], n // M, M) * tl[n % M] % M
        all2 += (cnt2 - cnt5) * (n // 10 * 4 + num[n % 10])
        res = res * now % M
        val *= 5
        cnt5 += 1
    a2 *= 2
    cnt2 += 1
res = res * quick_power(2, all2, M) % M
print(res)