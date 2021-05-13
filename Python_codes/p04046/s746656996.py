from math import factorial

mod = 10**9 + 7

H, W, A, B = map(int, input().split())
memo_fact = [1] * (H + W - 1)
memo_denometer = {}
for i in range(1, H + W - 1):
    memo_fact[i] = memo_fact[i - 1] * i % mod

def nCr(n,r):
    numerator = memo_fact[n]
    if (n, r) in memo_denometer:
        denometer = memo_denometer[(n, r)]
    else:
        denometer = pow(memo_fact[r], mod-2, mod) * pow(memo_fact[n-r], mod-2, mod)
    return (numerator * denometer) % mod

result = 0
for i in range(1, H - A + 1):
    result += (nCr((B-1)+(i-1), i-1) * nCr((W-B-1)+(H-i), W-B-1)) % mod
print(int(result % mod))