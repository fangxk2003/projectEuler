#include<bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 1e4;

LL res[N], f[N][32], ans[N];
int s[6], vis[32][32];

int main() {
    freopen("out.txt", "w", stdout);
    int k = 5, sta = (1 << k);
    for(int st = 0; st < sta; ++st) {
        int ST = st;
        for(int i = 0; i < k; ++i) {
            s[i] = ST & 1;
            ST >>= 1;a
        }
        if (s[0] == s[4] && s[1] == s[3]) continue;
        f[5][st] = 1;
        res[5] += f[5][st];
    }
    int n = 100;
    for (int now = 6; now <= n; ++now) {
        for(int st = 0; st < sta; ++st) {
            int ST = st;
            for(int i = 0; i < k; ++i) {
                s[i] = ST & 1;
                ST >>= 1;
            }
            if (s[0] == s[4] && s[1] == s[3]) continue;
            if (s[1] == s[4] && s[2] == s[3]) {
                s[5] = (s[0] ^ 1);
                if (!(s[5] == s[1] && s[2] == s[4])) {
                    f[now][st] = f[now - 1][(st >> 1) | (s[5] << 4)];
                    vis[st][(st >> 1) | (s[5] << 4)] = 1;
                }

            }
            else {
                if (s[2] == s[4]) {
                    s[5] = (s[1] ^ 1);
                    f[now][st] = f[now - 1][(st >> 1) | (s[5] << 4)];
                    vis[st][(st >> 1) | (s[5] << 4)] = 1;
                }
                else {
                    f[now][st] = f[now - 1][(st >> 1)] + f[now - 1][(st >> 1) | (1 << 4)];
                    vis[st][(st >> 1)] = 1;
                    vis[st][(st >> 1) | (1 << 4)] = 1;
                }
            }
            res[now] += f[now][st];
        }
    }
    for (int i = 5; i <= n; ++i) {
        printf("%lld\n", res[i]);
    }
    // for (int i = 0; i < 32; ++i) {
    //     for(int j = 0; j < 32; ++j) {
    //         printf("%d\t", vis[i][j]);
    //     }
    //     putchar('\n');
    // }
    fclose(stdout);
    return 0;
}