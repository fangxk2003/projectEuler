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
    LL x, y, MOD;
    printf("Calculate x ^ y % MOD\ninput x, y, MOD:\n");
    scanf("%lld%lld%lld", &x, &y, &MOD);
    printf("%lld\n", quiPow(x, y, MOD));
    return 0;
}