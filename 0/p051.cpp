#include<bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 1e6 + 10;

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

inline int getNum(int m, int x) {
    for(; x; x--) m /= 10;
    return m % 10;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n = 1e6;
    getPrimes(n);
    for(int i = 1e5; i <= n; ++i) {
        int L = (1 << 6);
        if (st[i]) continue;
        for(int sta = 1; sta < L; ++sta) {
            int now = -1;
            for(int k = 0; k < 6; ++k) {
                if ((sta >> k) & 1) {
                    if (now < 0) now = getNum(i, k);
                    else if (now != getNum(i, k)) {
                        now = -1;
                        break;
                    }
                }
            }
            if (now > -1 && now <= 2) {
                int cnt = 1, d = 0, p10 = 1;
                for(int k = 0; k < 6; ++k) {
                    if ((sta >> k) & 1) d += p10;
                    p10 *= 10;
                }
                int val = i;
                for(; now < 9; ++now) {
                    val += d;
                    if (!st[val]) cnt++;
                }
                if (cnt >= 8) {
                    printf("%d %d %d\n", i, d, cnt);
                    // return 0;
                }
            }
        }
    }
    return 0;
}