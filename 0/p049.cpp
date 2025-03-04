#include<bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 1e4 + 10;
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

inline int ll(int x) {
    int a[4];
    a[3] = x / 1000;
    a[2] = x / 100 % 10;
    a[1] = x / 10 % 10;
    a[0] = x % 10;
    sort(a, a + 4);
    return a[0] + a[1] * 10 + a[2] * 100 + a[3] * 1000;   
}

inline int check(int i, int j, int k) {
    int a = ll(i), b = ll(j), c = ll(k);
    if (a == b && b == c) return 1;
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n = 10000;
    getPrimes(n);
    for(int i = 1000; i < 10000; ++i) {
        if (st[i]) continue;
        for(int j = i + 1; j * 2 - i < 10000; ++j) {
            if (st[j]) continue;
            int k = j * 2 - i;
            if (st[k]) continue;
            if (check(i, j, k)) {
                cout << i << j << k << "\n";
            }
        }
    }
    return 0;
}