H, W, A, B = map(int, input().split())

MAX = 2 * 10 ** 5 + 1
MOD = 10 ** 9 + 7

# Factorial
fac = [0] * (MAX + 1)
fac[0] = 1
fac[1] = 1
for i in range(2, MAX + 1):
    fac[i] = fac[i - 1] * i % MOD
    
# Inverse factorial
finv = [0] * (MAX + 1)
finv[MAX] = pow(fac[MAX], MOD - 2, MOD)
for i in reversed(range(1, MAX + 1)):
    finv[i - 1] = finv[i] * i % MOD


def comb(a, b):
    return fac[a + b] * finv[a] * finv[b]


ans = 0
for i in range(B, W):
    ans += comb(i, H - A - 1) * comb(W - i - 1, A - 1) % MOD
    ans %= MOD

print(ans)
