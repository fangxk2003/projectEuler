#include<bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 200000;
int cnt2[N + 1], cnt5[N + 1];
int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int now = 2;
    while (now <= N) {
        for(int i = now; i <= N; i += now) {
            cnt2[i]++;
        }
        now <<= 1;
    }
    now = 5;
    while (now <= N) {
        for (int i = now; i <= N; i += now) {
            cnt5[i]++;
        }
        now *= 5;
    }
    for (int i = 1; i <= N; ++i) {
        cnt2[i] += cnt2[i - 1];
        cnt5[i] += cnt5[i - 1];
    }
    LL ans = 0;
    for (int a = N; a >= N / 3; --a) {
        cout << a << "\n";
        int l2 = cnt2[N] - cnt2[a], l5 = cnt5[N] - cnt5[a];
        if (l2 < 12 || l5 < 12) continue;
        l2 -= 12;
        l5 -= 12;
        for (int b = min(N - a, a), c = N - a - b; b >= c && c >= 0; --b, ++c) {
            if (l2 < cnt2[b] + cnt2[c] || l5 < cnt5[b] + cnt5[c]) continue;
            if (a == b && b == c) ans++;
            else if (a == b || b == c) ans += 3;
            else if (a > b && b > c) ans += 6;
        }
    }
    cout << ans << "\n";
    return 0;
}