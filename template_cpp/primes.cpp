int st[N], prime[N], k;
void getPrimes(int n) {
	st[1] = 1;
    for(int i = 2; i <= n; ++i) {
        if (!st[i]) prime[++k] = i;
		for(int j = 1; prime[j] <= n / i; ++j) {
            st[prime[j] * i] = 1;
            if (i % prime[j] == 0) break;
        }
	}
}