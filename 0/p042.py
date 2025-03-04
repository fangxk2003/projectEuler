myFile = open("C:/Users/Klaus/Desktop/PE/P42/p042_words.txt", 'r')
a = list(map((lambda x : x[1 : -1]), myFile.readline().split(',')))
print(a)
cnt = 0
for s in a :
    num = 0
    for ch in s :
        num += ord(ch) - ord('A') + 1
    num *= 2
    x = int(num ** 0.5)
    if (x * (x + 1) == num) : cnt += 1
print(cnt)