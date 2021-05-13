H,W,A,B = map(int,input().split())

N = H+W+10
MOD = 10**9+7

fac = [1,1] + [0]*N
finv = [1,1] + [0]*N
inv = [0,1] + [0]*N
for i in range(2,N+2):
    fac[i] = fac[i-1] * i % MOD
    inv[i] = -inv[MOD%i] * (MOD // i) % MOD
    finv[i] = finv[i-1] * inv[i] % MOD

def ncr(n,r):
    if n < r: return 0
    if n < 0 or r < 0: return 0
    return fac[n] * (finv[r] * finv[n-r] % MOD) % MOD

ans = 0
for i in range(W-B):
    ans += ncr(H-1-A+B+i, H-1-A) * ncr(A-1+W-1-B-i, A-1)
    ans %= MOD
print(ans)