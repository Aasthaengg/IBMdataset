MOD = 10 ** 9 + 7
fac = [1] * 200005
for i in range(len(fac) - 1):
    fac[i + 1] = fac[i] * (i + 1) % MOD
h, w, a, b = map(int, input().split())
ans = 0
x, y = b, h - a - 1
while x < w and y >= 0:
    p = w - x - 1
    q = h - y - 1
    ans += (fac[x + y] * pow(fac[x] * fac[y], MOD - 2, MOD) *
            fac[p + q] * pow(fac[p] * fac[q], MOD - 2, MOD)) % MOD
    x += 1
    y -= 1
print(ans % MOD)