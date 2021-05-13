H, W, A, B = map(int, input().split())

mod = 10 ** 9 + 7

# 階乗
fac = [1] * (H + W - 2)
# 逆元
inv = [1] * (H + W - 2)
for i in range(1, H + W - 2):
    fac[i] = (fac[i - 1] * i) % mod
    inv[i] = pow(fac[i], mod - 2, mod)


def f(x, y):
    res = fac[x + y] * inv[x] * inv[y]
    return res % mod


ans = 0
for x in range(B, W):
    ans += f(x, H - A - 1) * f(W - 1 - x, A - 1)
print(ans % mod)

