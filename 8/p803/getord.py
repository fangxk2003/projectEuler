# while(1):
#     c = input()
#     if c >= 'a' : print(ord(c) - ord('a'))
#     else : print(ord(c) - ord('A') + 26)

# c = [41, 20, 25, 25, 11, 4, 40, 13, 4]

# d = 1
# k = 25214903917
# now = 0
# p16 = 2 ** 16
# vis = [0] * p16
# for i in range(0, p16 + 1) :
#     if vis[d] == 0 :
#         vis[d] = 1
#         d = (k * d + 11) % p16
#     else :
#         print(d, i)
#         exit()



# c = [41, 20, 25, 25, 11, 4, 40, 13, 4]
# c = [37, 20, 2, 10, 24, 45, 4, 23, 19]
c = [1, 42, 50, 8, 2, 39, 32, 28, 50]
d = 1
k = 25214903917
now = 0
p16 = 2 ** 16
fd = 0
for i in range(123456, 123456 + 1) :
    d = i
    for now in range(0, 8) :
        if (k * c[now] + int((k * d + 11) / p16)) % 52 == c[now + 1] :
            if (now > 1) : print(now)
        else :
            break
        d = (k * d + 11) % p16
    # d = (k * dd + 11) % p16

