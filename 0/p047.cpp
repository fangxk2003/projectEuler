#include<bits/stdc++.h>
using namespace std;
const int N = 1e6 + 10;

int prime[N], st[N], k, cnt[N];

int getPrimes(int n) {
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
    int n = 1e6;
    getPrimes(n);
    printf("%d\n", k);
    for(int i = 1; i <= k; ++i) {
        for(int j = prime[i]; j <= n; j += prime[i]) {
            cnt[j]++;
        }
    }
    for(int i = 1; i <= n; ++i) {
        if (cnt[i] == 4 && cnt[i + 1] == 4 && cnt[i + 2] == 4 && cnt[i + 3] == 4) {
            printf("%d\n", i);
            return 0;
        }
    }
    return 0;
}