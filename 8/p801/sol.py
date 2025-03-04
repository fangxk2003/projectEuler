import math

for n in range(2, 10):
    ans = 0
    for i in range(1, n * n - n + 1):
        for j in range(1, n * n - n + 1):
            if ((i ** j) % n == (j ** i) % n):
                ans += 1
    print(ans)