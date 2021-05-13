H,W,A,B = map(int,input().split())

U = 2*(10**5)
MOD = 10**9 + 7

fact = [1]*(U+1)
fact_inv = [1]*(U+1)
for i in range(1, U+1) :
    fact[i] = (fact[i-1] * i) % MOD
fact_inv[U] = pow(fact[U], MOD-2, MOD)
for i in range(U,0,-1) :
    fact_inv[i-1] = (fact_inv[i] * i) % MOD

def comb(n, k) :
    if k < 0 or k > n :
        return 0
    x = fact[n]
    x *= fact_inv[k]
    x %= MOD
    x *= fact_inv[n-k]
    x %= MOD
    return x

ans = 0
for x in range(B,W) :
    if x == B :
        ans += comb(H-A-1+x, x) * comb(A+W-1-x, W-1-x)
    else :
        ans += (comb(H-A-1+x, x) - comb(H-A-1+x-1, x-1)) * comb(A+W-1-x, W-1-x)
    ans %= MOD
print(ans)
