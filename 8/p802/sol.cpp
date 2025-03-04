#include<bits/stdc++.h>
using namespace std;
using LL = long long;

const int N = 1e7 + 10, M = 1e6;
const int MOD = 1020340567;

char st[N], mu[N];
int prime[M], p2[N], k;

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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n = 1e7;
    LL ans = 0;
    p2[0] = 1;
    initMobius(n);
    printf("%d\n", k);
    printf("%d %d\n", mu[8], mu[30]);
    for(int i = 1; i <= n; ++i) {
        p2[i] = p2[i - 1] * 2 % MOD;
    }
    for(int d = 1; d <= n; ++d) {
        ans += mu[d] * p2[n / d];
    }
    printf("%lld\n", ans);
    ans %= MOD;
    ans += MOD;
    printf("%lld\n", ans);
    return 0;
}