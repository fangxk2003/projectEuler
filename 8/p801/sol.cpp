#include<bits/stdc++.h>
using namespace std;
using LL = long long;

const LL MOD = 993353399;
const int N = 1e5;
LL pr[N];
int cnt[N], tot;

inline LL mul(LL x, LL y, LL n) {
    LL res = 0;
    while(y) {
        if (y & 1) res = (res + x) % n;
        x = (x + x) % n;
        y >>= 1;
    }
    return res;
}

inline LL qui_pow(LL x, LL y, LL n) {
    LL res = 1;
    while (y) {
        if (y & 1) res = mul(res, x, n);
        x = mul(x, x, n);
        y >>= 1;
    }
    return res;
}

inline LL qui_Pow(LL x, LL y) {
    LL res = 1;
    x %= MOD;
    if (y == 0) return 1;
    while (y) {
        if (y & 1) res = res * x % MOD;
        x = x * x % MOD;
        y >>= 1;
    }
    return res;
}

inline int Miller_Rabin(LL n) {
    if (n == 2) return 1;
    if (n % 2 == 0) return 0;
    LL m = n - 1, k = 0;
    while(!(m & 1)) {
        m >>= 1;
        ++k;
    }
    int T = 20;
    while(T--) {
        LL a = rand() % (n - 1) + 1;
        LL x = qui_pow(a, m, n), y;
        for(int i = 0; i < k; ++i) {
            y = mul(x, x, n);
            if (y == 1 && x != 1 && x != n - 1) return 0;
            x = y;
        }
        if (y != 1) return 0;
    }
    return 1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    srand(time(0));
    LL ans = 0;
    for(LL n = 1e16; n <= 1e16 + 1e6; ++n) {
        memset(cnt, 0, sizeof cnt);
        memset(pr, 0, sizeof pr);
        tot = 0;
        if (Miller_Rabin(n)) {
            printf("%lld\n", n);
            LL m = n - 1;
            LL p = 2;
            ans += qui_Pow(m, 2) % MOD;
            if (ans >= MOD) ans -= MOD;
            while(p * p <= m) {
                if (m % p == 0) {
                    pr[tot] = p;
                    while(m % p == 0) {
                        m /= p;
                        cnt[tot]++;
                    }
                    tot++;
                }
                p++;
            }
            if (m > 1) {
                pr[tot] = m;
                cnt[tot++] = 1;
            }
            int all = 1;
            for(int i = 0; i < tot; ++i) {
                all *= (cnt[i] + 1);
            }
            for(int i = 0; i < all; ++i) {
                for(int j = 0; j < all; ++j) {
                    LL res = 1;
                    int ii = i, jj = j;
                    for(int k = 0; k < tot; ++k) {
                        int pi = ii % (cnt[k] + 1), pj = jj % (cnt[k] + 1);
                        if (pi > pj) swap(pi, pj);
                        if (pi == 0) {
                            if (pj == 0) res = res * qui_Pow(pr[k], cnt[k] * 2) % MOD;
                            else res = res * qui_Pow(pr[k] - 1, 1) % MOD * qui_Pow(pr[k], cnt[k] * 2 - 1) % MOD;
                        }
                        else res = res * qui_Pow(pr[k] - 1, 2) % MOD * qui_Pow(pr[k], cnt[k] * 2 - 2 + pi) % MOD;
                        ii /= (cnt[k] + 1);
                        jj /= (cnt[k] + 1);
                    }
                    ans += res;
                    if (ans >= MOD) ans -= MOD;
                }
            }
        }
    }
    printf("%lld\n", ans);
    // for(LL n = 1e16; n <= 1e16 + 1e6; ++n) {

    // }
    return 0;
}

//没看见只要素数啊啊啊