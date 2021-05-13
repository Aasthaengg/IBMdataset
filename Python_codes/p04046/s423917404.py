H, W, A, B = map(int, input().split())

mod = 10**9 + 7

fact = [1] * (H + W - 1)
invfact = [1] * (H + W - 1)

for i in range(1, H + W - 1):
    fact[i] = fact[i - 1] * i % mod
for i in range(1, H + W - 1):
    invfact[i] = pow(fact[i], mod-2, mod)

def nCr(n,r):
    return fact[n] * invfact[r] * invfact[n-r]

result = 0
for i in range(1, H - A + 1):
    result += (nCr((B-1)+(i-1), i-1) * nCr((W-B-1)+(H-i), W-B-1)) % mod
print(int(result % mod))