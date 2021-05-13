H, W, A, B = map(int, open(0).read().split())
MOD = 10**9+7

def modperm(m, n, mod):
    p = 1
    for i in range(n):
        p = p * (m - i) % mod
    return p

def modcomb(m, n, mod):
    if n > m - n:
        n = m - n
    p = modperm(m, n, mod)
    q = pow(modperm(n, n, mod), mod - 2, mod)
    return p * q % mod

total = modcomb(H + W - 2, W - 1, MOD)

tmp = modcomb(A + W - 2, W - 1, MOD)
total -= tmp

for i in range(B - 1):
    a = H - A + i
    b = i + 1
    c = W - i - 1
    d = W + A - 2 - i
#     print(a,b,c,d)
    tmp = tmp * a * c % MOD
    tmp = tmp * pow(b, MOD - 2, MOD) % MOD
    tmp = tmp * pow(d, MOD - 2, MOD) % MOD
#     print(tmp)
    total = (total - tmp) % MOD

print(total)