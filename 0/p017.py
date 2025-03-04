num = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
numty = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
ans = 0
for i in range(1, 20):
    ans += len(num[i])
for i in range(20, 100):
    ans += len(numty[i // 10]) + len(num[i % 10])
ans *= 10
for i in range(1, 10):
    ans += (len(num[i]) + 7) * 100 + 3 * 99
ans += 11
print(ans)