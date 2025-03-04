from utils import linear_prime_sieve
import heapq
primes, is_prime, phi = linear_prime_sieve(10 ** 7)
print(len(primes))
print(primes[0])
ans = 1
cnt = 0
heap = []
for prime in primes:
    heapq.heappush(heap, prime)
for i in range(500500) :
    min_item = heapq.heappop(heap)
    heapq.heappush(heap, min_item * min_item)
    ans = ans * min_item % 500500507
print(ans)