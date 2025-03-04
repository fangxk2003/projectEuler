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


srand(time(0));