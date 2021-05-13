import math
MOD = 10 ** 9 + 7
H, W, A, B = map(int, input().split())
maxf = H + W

f, invf = [1] * maxf, [1] * maxf

for i in range(1, maxf):
    f[i] = i * f[i - 1] % MOD
invf[maxf - 1] = pow(f[maxf - 1], MOD - 2, MOD)
for i in range(maxf - 1, 0, -1):
    invf[i - 1] = invf[i] * i % MOD

comb = lambda a, b: f[a + b] * invf[a] * invf[b] % MOD

ans = 0
for x in range(B, W):
    ans += comb(x, H - A - 1) * comb(W - 1 - x, A - 1) % MOD
print(ans % MOD)