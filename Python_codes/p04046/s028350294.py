h, w, a, b = map(int, input().split())

MOD = 10 ** 9 + 7
f = [1] * 300005
for i in range(2, 300005):
    f[i] = (f[i - 1] * i) % MOD

def comb(k, n):
    if n < k:
        return 0
    if k == 0 or n == k:
        return 1
    return (f[n] * pow(f[k], MOD - 2, MOD) * pow(f[n - k], MOD - 2, MOD)) % MOD

ans = 0
for i in range(h - a):
    ans += comb(i, i + b - 1) * comb(w - b - 1, w + h - 2 - i - b) % MOD
    ans %= MOD
print(ans)

