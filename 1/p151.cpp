#include<bits/stdc++.h>
#include<windows.h>
#define int long long
using namespace std;
using LL = long long;
map<multiset<int>, double> mp;
multiset<int> oi;
void dfs(multiset<int> now) {
    if (mp.find(now) != mp.end()) return;
    double res = 0;
    multiset<int> nn;
    for(auto it = now.begin(); it != now.end(); it++) {
        nn = now;
        for (auto itn = nn.begin(); itn != nn.end(); itn++) {
            if (*itn == *it) {
                if (*itn == 1) nn.erase(itn);
                else {
                    int x = *itn / 2;
                    nn.erase(itn);
                    nn.insert(x);
                    x /= 2;
                    while (x >= 1) {
                        nn.insert(x);
                        x /= 2;
                    }
                }
                dfs(nn);
                res += mp[nn];
                break;
            }
        }
    }
    if (now.size() == 1) res += 1;
    else res /= now.size();
    mp[now] = res;
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    multiset<int> ori;
    ori.insert(1);
    oi = ori;
    mp[ori] = 1;
    ori.clear();
    ori.insert(16);
    dfs(ori);
    printf("%.6f\n", mp[ori] - 2);
    return 0;
}