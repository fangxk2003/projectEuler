int st[N], prime[N], phi[N], k;

void getPhi(int n) {
	st[1] = 1;
    phi[1] = 1;
    for(int i = 2; i <= n; ++i) {
        if (!st[i]) {
            prime[++k] = i;
            phi[i] = i - 1;
        }
		for(int j = 1; prime[j] <= n / i; ++j) {
            st[prime[j] * i] = 1;
            if (i % prime[j] == 0) {
                phi[i * prime[j]] = phi[i] * prime[j];
                break;
            } 
            else phi[i * prime[j]] = phi[i] * (prime[j] - 1);
        }
	}
}
