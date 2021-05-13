H, W, A, B = map(int, input().split())
M = 10 ** 5 + 5
M *= 2
fact = [0] * M
rfact = [0] * M
fact[0] = 1
MOD = 10 ** 9 + 7
for i in range(1, M):
    fact[i] = fact[i - 1] * i % MOD

rfact[M - 1] = pow(fact[M - 1], MOD - 2, MOD)
for i in range(M - 2, -1, -1):
    rfact[i] = rfact[i + 1] * (i + 1) % MOD


def comb(n, k):
    return fact[n] * rfact[n - k] * rfact[k] % MOD


num = 0
for i in range(B + 1, W + 1):
    num += comb(H - (A + 1) + i - 1, i - 1) * comb(W - i + A - 1, A - 1)
    num %= MOD

print(num)