h, w, a, b = map(int, input().split())
m = h + w
mod = 10 ** 9 + 7

fac = [1] * (m + 1)
inv = [1] * (m + 1)
for i in range(1, m + 1):
    fac[i] = fac[i - 1] * i % mod
inv[-1] = pow(fac[-1], mod - 2, mod)
for i in range(m - 1, -1, -1):
    inv[i] = inv[i + 1] * (i + 1) % mod


def cmb(n, r):
    assert n >= r >= 0
    ret = fac[n] 
    ret *= inv[n - r]
    ret %= mod
    ret *= inv[r]
    return ret % mod


ans = sum(cmb(h - a + i - 1, i) * cmb(a + w - 2 - i, a - 1) % mod for i in range(b, w))
print(ans % mod)