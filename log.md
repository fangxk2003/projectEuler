https://projecteuler.net/action=redirect;post_id=111677

Here is a solution that is more efficient than the sieve of Eratosthenes. It is derived from similar algorithms for [counting primes](https://en.wikipedia.org/wiki/Prime-counting_function). The advantage is that there is no need to find all the primes to find their sum.

The main idea is as follows: Let S(v,m) be the sum of integers in the range 2..v that remain after sieving with all primes smaller or equal than m.

That is S(v,m) is the sum of integers up to v that are either prime or the product of primes larger than m.  S(v, p) is equal to S(v, p-1) if p is not prime or v is smaller than p*p. Otherwise (p prime, p*p<=v) S(v,p) can be computed from S(v,p-1) by finding the sum of integers that are removed while sieving with p. An integer is removed in this step if it is the product of p with another integer that has no divisor smaller than p. This can be expressed as
$$
S(v,p)=S(v,p−1)−p(S(v/p,p−1)−S(p−1,p−1)).
$$
Dynamic programming can be used to implement this. It is sufficient to compute S(v,p) for all positive integers v that are representable as floor(n/k) for some integer k and all $$p≤\sqrt{v}$$

```python
def P10(n):
    r = int(n**0.5)
    assert r*r <= n and (r+1)**2 > n
    V = [n//i for i in range(1,r+1)]
    V += list(range(V[-1]-1,0,-1))
    S = {i:i*(i+1)//2-1 for i in V}
    for p in range(2,r+1):
        if S[p] > S[p-1]:  # p is prime
            sp = S[p-1]  # sum of primes smaller than p
            p2 = p*p
            for v in V:
                if v < p2: break
                S[v] -= p*(S[v//p] - sp)
    return S[n]
```



The complexity of this algorithm is about $$O(n^{0.75})$$ and needs 9 ms to find the solution. Computing the sum of primes up to different bounds n gives:

n = 2e7: 12272577818052  0.04s

n = 2e8: 1075207199997334  0.2s

n = 2e9: 95673602693282040  1s

n = 2e10: 8617752113620426559  6.2s

n = 2e11: 783964147695858014236  34s

n = 2e12: 71904055278788602481894  3 min

I also have a C++ version of this algorithm. This one solves the problem in 700μs. It needs 10 hours to compute the sum of primes up to 1e17 which is 129408626276669278966252031311350.

It is also possible to improve the complexity of the algorithm to $$O(n^{2/3})$$ , but the code would be more complex.



## Meissel-Lehmer

