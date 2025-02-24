n = 10 ** 5
is_prime = [True for _ in range(0, n + 1)]
rad = [0 for _ in range(0, n + 1)]
primes = []
rad[1] = 1
for i in range(2, n + 1):
    if is_prime[i]:
        primes.append(i)
        rad[i] = i
    for prime in primes:
        if i * prime > n:
            break
        is_prime[i * prime] = False
        if i % prime == 0:
            rad[i * prime] = rad[i]
            break
        rad[i * prime] = rad[i] * prime

arr = sorted([i for i in range(0, n + 1)], key = lambda i : (rad[i], i))
print(arr[10000])

# 21417
