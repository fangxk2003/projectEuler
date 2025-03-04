from math import sqrt
now = 13 * 10 ** 2000
rt = 3 * 10 ** 1000
lst = 0
while lst != rt:
    lst = rt
    rt = (rt + now // rt) // 2
digit_sum = sum(int(digit) for digit in str(rt))
print(digit_sum - 3)