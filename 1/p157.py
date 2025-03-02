from utils import factor_count

res = 0
for n in range(1, 10) :
    for a2 in range(0, n + 2) :
        for b2 in range(0, n + 2) :
            for a5 in range(0, n + 2) :
                for b5 in range(0, n + 2) :
                    aa2 = a2 - min(a2, b2)
                    bb2 = b2 - min(a2, b2)
                    aa5 = a5 - min(a5, b5)
                    bb5 = b5 - min(a5, b5)
                    num = 2 ** aa2 * 5 ** aa5 + 2 ** bb2 * 5 ** bb5
                    if num % 2 == 0 : num //= 2
                    elif a2 == n + 1 or b2 == n + 1 : continue
                    if num % 5 == 0 : num //= 5
                    elif a5 == n + 1 or b5 == n + 1 : continue
                    res += factor_count(num)
                    if a2 == b2 and a5 == b5 : res += factor_count(num)
                    # print(a2, b2, a5, b5, 2 ** a2 * 5 ** a5 + 2 ** b2 * 5 ** b5)
print(res // 2)