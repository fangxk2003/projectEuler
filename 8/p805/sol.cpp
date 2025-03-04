#include<bits/stdc++.h>
using namespace std;
using LL = long long;
const int M = 200;
const int N = M * M * M * 10;
const int MOD = 1e9 + 7;

int st[N], prime[N / 10], phi[N], k;

void getPhi(int n) {
	st[1] = 1;
    phi[1] = 1;
    for(int i = 2; i <= n; ++i) {
        if (!st[i]) {
            prime[++k] = i;
            phi[i] = i - 1;
        }
		for(int j = 1; prime[j] <= n / i; ++j) {
            st[prime[j] * i] = 1;
            if (i % prime[j] == 0) {
                phi[i * prime[j]] = phi[i] * prime[j];
                break;
            } 
            else phi[i * prime[j]] = phi[i] * (prime[j] - 1);
        }
	}
}

inline int gcd(int x, int y) {
    if (x == 0) return y;
    return gcd(y % x, x);
}

inline LL quiPow(LL x, LL y, LL M) {
    LL res = 1;
    x %= M;
    while(y) {
        if (y & 1) res = res * x % M;
        x = x * x % M;
        y >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    getPhi(N - 1);
    LL ans = 0;
    for (int u = 1; u <= M; ++u) {
        for(int v = 1; v <= M; ++v) {
            // printf("%d %d\n", u, v);
            if (gcd(u, v) > 1) continue;
            LL X = v * v * v * 10 - u * u * u;
            LL minm = 1e9, mina = 0;
            for (int a = 1; a <= 9; ++a) {
                if ((a + 1) * u * u * u > 10 * v * v * v) continue;
                if ((a + 1) * u * u * u == 10 * v * v * v && (a - 10) * v * v * v + u * u * u < 0) continue;
                // if (v == 1) printf("%d\n", u);
                int XX = X / gcd(a, X);
                if (XX <= 0 || XX % 2 == 0 || XX % 5 == 0) continue;
                int ed = sqrt(phi[XX]), m = 0, mm = phi[XX];
                for(int D = 1; D <= ed; ++D) {
                    if (phi[XX] % D == 0) {
                        if (quiPow(10, D, XX) == 1) {
                            m = D;
                            break;
                        }
                        if (quiPow(10, phi[XX] / D, XX) == 1) mm = phi[XX] / D;
                    }
                }
                if (!m) m = mm;
                if (m < minm) {
                    minm = m;
                    mina = a;
                }
            }
            if (mina == 0) continue;
            // printf("%d %d %lld %lld\n", u, v, minm, mina);
            LL b = 1LL * mina * ((quiPow(10, minm - 1, MOD) % MOD * (u * u * u) + MOD - v * v * v) % MOD) % MOD * quiPow(X, MOD - 2, MOD);
            ans += 1LL * mina * quiPow(10, minm - 1, MOD) % MOD + b;
            ans %= MOD;
        }
    }
    ans %= MOD;
    printf("%lld\n", ans);
    return 0;
}