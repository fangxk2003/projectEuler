#include<bits/stdc++.h>
using namespace std;
using LL = long long;


inline LL quiPow(LL x, LL y, LL MOD) {
    LL res = 1;
    x %= MOD;
    while (y > 0) {
        if (y & 1) res = res * x % MOD;
        x = x * x % MOD;
        y >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int k = 1e4;
    LL n = 1e12;
    for (LL p = 2e9; p <= 2e9 + 2000; ++p) {
        int flag = 0;
        for (LL d = 2; d * d <= p; ++d) {
            if (p % d == 0){
                flag = 1;
                break;
            }
        }
        if (flag) continue;
        pow[0] = 1;
        for (int i = 1; i <= k + 1; ++i) {
            pow[i] = pow[i - 1] * i % p;
        }
        inv[k + 1] = quiPow(pow[k + 1], p - 2, p);
        for(int i = k; i >= 0; --i) {
            inv[i] = inv[i + 1] * (i + 1) % p;
        }
        c[0][1] = 1;
        for(int i = 1; i <= k; ++i) {
            LL inv_ip1 = quiPow(i + 1, p - 2, p);
            for(int j = 0; j < i; ++j) {
                c[i][j] += 
            }
        }
    }
    return 0;
}