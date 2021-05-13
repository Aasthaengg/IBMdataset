mod = 10**9 + 7
N = 200000
fact = [None] * (N+1)
fact[0] = 1
for i in range(1, N+1):
    fact[i] = fact[i-1] * i % mod

def comb(n, k):
    return fact[n] * pow(fact[k], mod-2, mod) * pow(fact[n-k], mod-2, mod) % mod

H, W, A, B = map(int, input().split())
ans = 0
for b in range(B+1, W+1):
    tmp = comb(H-A+b-2, b-1) * comb(A+W-b-1, A-1) % mod
    ans = (ans + tmp) % mod
print(ans)
