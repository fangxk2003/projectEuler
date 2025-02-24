import gmpy2

current = 2 
id = 1
while (2 * id * current <= 10 ** 10) :
    current = gmpy2.next_prime(current)
    id += 1
if (id % 2 == 0) : id += 1
print(id)
# 21035