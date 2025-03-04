const int N = 1e6 + 10;

char st[N], mu[N];
int prime[N], k;

void initMobius(int n) {
	st[1] = 1;
    mu[1] = 1;
    for(int i = 2; i <= n; ++i) {
        if (!st[i]) {
            prime[++k] = i;
            mu[i] = -1;
        }
		for(int j = 1; prime[j] <= n / i; ++j) {
            st[prime[j] * i] = 1;
            if (i % prime[j] == 0) {
                mu[i * prime[j]] = 0;
                break;
            }
            else mu[i * prime[j]] = -mu[i];
        }
	}
}