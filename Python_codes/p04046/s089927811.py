H, W, A, B = map(int,input().split())
MOD = 10**9 + 7

fac = [1 for k in range(200010)]
inv = [1 for k in range(200010)]
finv = [1 for k in range(200010)]

for k in range(2,200010):
    fac[k] = (fac[k-1]*k)%MOD
    inv[k] = (MOD - inv[MOD%k] * (MOD // k))%MOD
    finv[k] = (finv[k - 1] * inv[k]) % MOD;

def nCr(n,r):
    return (fac[n]*finv[r]*finv[n-r])%MOD

k = 1
ans = 0
while B+k <= W and H-A-k+1 > 0:
    ans += nCr(B+k-1+(H-A-k),B+k-1) * nCr(W-(B+k) + H-(H-A-k+1),H-(H-A-k+1))
    ans %= MOD
    k += 1
print(ans)
