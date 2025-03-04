#include<bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 1e6 + 10;
LL st[N], prime[N], k;
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
    int n = 1e6;
    getPrimes(n);
    LL ans = 0;
    int len = 0;
    for(int i = 1; i <= k; ++i) prime[i] += prime[i - 1];
    for(int i = 1; i <= k; ++i) {
        for(int j = 0; j < i; ++j) {
            LL now = prime[i] - prime[j];
            if (now < 1000000 && !st[now]) {
                if (i - j > len) {
                    len = i - j;
                    ans = now;
                }
            }
        }
    }
    cout << ans << "\n";
    return 0;
}