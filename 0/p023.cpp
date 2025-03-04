#include<bits/stdc++.h>
using namespace std;
using LL = long long;

inline int val(int x) {
    int res = 1;
    for(int i = 2; i * i <= x; ++i) {
        if (x % i == 0) {
            if (i * i == x) res += i;
            else res += i + x / i;
        }
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n = 28123;
    vector<int> vis(n + 1, 0);
    vector<int> all;
    for(int i = 1; i <= n; ++i) {
        if (val(i) > i) all.push_back(i);
    }
    for(int x : all) for(int y : all) {
        if (x + y <= n) vis[x + y] = 1;
    }
    int ans = 0;
    for(int i = 1; i <= n; ++i) {
        if (!vis[i]) ans += i;
    }
    printf("%d\n", ans);
    return 0;
}