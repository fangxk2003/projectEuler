#include<bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 1e8, M = 1e4 + 10, T = 1e5;
unsigned short d[N + 1];
int id[1000];
int st[M], prime[M], k;
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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    getPrimes(10000);
    for (int x = 1; x <= N; ++x) {
        if (x % 1000000 == 0) printf("%d\n", x);
        int X = x;
        d[x] = 1;
        for (int i = 1; i <= k; ++i) {
            if (prime[i] * prime[i] > X) break;
            if (X % prime[i] == 0) {
                int cnt = 1;
                while(X % prime[i] == 0) {
                    X /= prime[i];
                    cnt++;
                }
                d[x] *= cnt;
            }
        }
        if (X > 1) d[x] *= 2;
    }
    int now = 1, hd = 1;
    id[1] = 1;
    for (int n = 2; n <= T; ++n) {
        while(now >= hd && d[id[now]] <= d[n]) now--;
        id[++now] = n;
    }
    LL ans = d[id[1]];
    for (int n = T + 1; n <= N; ++n) {
        if (n - T == id[hd]) hd++;
        while(now >= hd && d[id[now]] <= d[n]) now--;
        id[++now] = n;
        ans += d[id[hd]];
    }
    printf("%lld\n", ans);
    printf("%d\n", hd);
    return 0;
}