def linear_prime_sieve(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    phi = [0] * (n + 1)
    phi[1] = 1
    for i in range(2, n + 1):
        if is_prime[i] :
            phi[i] = i - 1
            primes.append(i)
        for prime in primes:
            if prime * i > n : break
            is_prime[prime * i] = False
            if i % prime == 0 :
                phi[prime * i] = phi[i] * prime
                break
            else : phi[prime * i] = phi[i] * (prime - 1)
    return primes, is_prime, phi