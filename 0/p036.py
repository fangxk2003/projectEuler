sum = 0
for i in range(1, 1000000) :
    if (str(i) == str(i)[::-1] and bin(i).replace('0b', '') == bin(i).replace('0b', '')[::-1] ) : sum += i
print(sum)