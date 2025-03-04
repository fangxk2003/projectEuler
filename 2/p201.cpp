#include<bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 400000;
int dp[2][52][N];

int main() {
    int maxi = 0;
    for(int i = 1; i <= 100; ++i) {
        int now = i & 1, lst = now ^ 1;
        dp[lst][0][0] = 1;
        memset(dp[now], 0, sizeof dp[now]);
        for(int j = 0; j <= 50; ++j) {
            for(int k = 0; k <= maxi; ++k) {
                dp[now][j + 1][k + i * i] += dp[lst][j][k];
                dp[now][j][k] += dp[lst][j][k];
            }
        }
        maxi += i * i;
    }
    LL sum = 0;
    cout << maxi << "\n";
    for(int i = 1; i <= maxi; ++i) {
        if (dp[0][50][i] == 1) sum += i;
    }
    cout << sum << "\n";
    return 0;
}