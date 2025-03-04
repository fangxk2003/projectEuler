#include<bits/stdc++.h>
using namespace std;
using LL = long long;
const LL K = 1e4;
const LL N = 1e12;

LL powe[K + 10], inv[K + 10], b[K + 10], c[K + 10];
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

inline void getBernoulli(int N, LL MOD) {
    powe[0] = 1;
    for(int i = 1; i <= N + 1; ++i) powe[i] = powe[i - 1] * i % MOD;
    inv[N + 1] = quiPow(powe[N + 1], MOD - 2, MOD);
    for(int i = N; i >= 0; --i) inv[i] = inv[i + 1] * (i + 1) % MOD;

    b[0] = 1;
    for (int n = 1; n <= N; ++n) {
        b[n] = 0;
        for(int k = 0; k < n; ++k) {
            b[n] += powe[n + 1] * inv[k] % MOD * inv[n + 1 - k] % MOD * b[k] % MOD;
            if (b[n] >= MOD) b[n] -= MOD;
        }
        b[n] = quiPow(n + 1, MOD - 2, MOD) * (MOD - b[n]) % MOD;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    LL ans = 0;
    for (LL p = 2e9; p <= 2e9 + 2000; ++p) {
        int flag = 0;
        for (LL d = 2; d * d <= p; ++d) {
            if (p % d == 0){
                flag = 1;
                break;
            }
        }
        if (flag) continue;
        printf("%lld\n", p);
        getBernoulli(K + 3, p);
        for(int k = 0; k <= K; ++k)
            c[K - k + 1] = quiPow(K + 1, p - 2, p) * powe[K + 1] % p * inv[K + 1 - k] % p * inv[k] % p * b[k] % p;
        c[K]++;
        LL pn = N % p;
        LL now = pn;
        LL res = 0, res1 = 0, res2 = 0;
        for(int j = 1; j <= K + 1; ++j) {
            res1 += c[j] * now % p;
            if (res1 >= p) res1 -= p;
            now = now * pn % p;
        }
        res1 = res1 * (N + 1) % p;

        for(int k = 0; k <= K + 1; ++k)
            c[K - k + 2] = quiPow(K + 2, p - 2, p) * powe[K + 2] % p * inv[K + 2 - k] % p * inv[k] % p * b[k] % p;
        c[K + 1]++;
        now = pn;
        for(int j = 1; j <= K + 2; ++j) {
            res2 += c[j] * now % p;
            if (res2 >= p) res2 -= p;
            now = now * pn % p;
        }
        res = res1 - res2;
        if (res < 0) res += p;
        ans += res;
    }
    printf("%lld\n", ans);
    return 0;
}