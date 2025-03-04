sum = 0
for _ in range(0, 100):
    sum += int(input())
while sum >= 1e10:
    sum = sum // 10
print(sum)