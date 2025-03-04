#include<bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 1e4;
const LL MOD = 1e9;
const int trans[6][6] = {{0, 1, 0, 1, 0, 0},
                         {1, 0, 1, 0, 0, 0},
                         {0, 1, 0, 0, 0, 1},
                         {1, 0, 0, 0, 1, 0},
                         {0, 0, 0, 1, 0, 1},
                         {0, 0, 1, 0, 1, 0}};

LL now[N + 10][6], E[6];
int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    now[1][1] = 1;
    LL a = 3, b = 6, c = 9, k = 10;
    LL ans = (c - 1) * (c - 1) - (a - 1) * (a - 1) + (k - a) * (k - a) - (k - b) * (k - b);
    for(int n = 2; n <= N; ++n) {
        a = a * 3 % MOD;
        b = b * 6 % MOD;
        c = c * 9 % MOD;
        k = k * 10 % MOD;
        E[0] = (b - 1) * (b - 1) - (a - 1) * (a - 1);
        E[1] = (c - 1) * (c - 1) - (a - 1) * (a - 1);
        E[2] = (c - 1) * (c - 1) - (b - 1) * (b - 1);
        E[3] = (k - a) * (k - a) - (k - b) * (k - b);
        E[4] = (k - a) * (k - a) - (k - c) * (k - c);
        E[5] = (k - b) * (k - b) - (k - c) * (k - c);
        for(int i = 0; i < 6; ++i) {
            E[i] %= MOD;
            if (E[i] < 0) E[i] += MOD;
        }
        for(int i = 0; i < 6; ++i)
            for(int j = 0; j < 6; ++j)
                if (trans[i][j]) now[n][i] += now[n - 1][j];
        now[n][1]++;
        now[n][3]++;
        now[n][5]++;
        for (int i = 0; i < 6; ++i) now[n][i] %= MOD;
        now[n][3]++;
        for (int i = 0; i < 6; ++i) {
            ans += now[n][i] * E[i] % MOD;
        }
        now[n][3]--;
    }
    ans %= MOD;
    printf("%lld\n", ans);
    return 0;
}
