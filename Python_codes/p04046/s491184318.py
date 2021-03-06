# nの逆元のリスト
def inv_mod(n:int, mod:int) -> list:
    inv = [0,1]
    for i in range(2,n+1):
        inv.append(mod - ((mod//i)*inv[mod%i]) % mod)
    return inv
       
# nの階乗のリスト
def fact(n:int, mod:int) -> list:
    fac = [1,1]
    res = 1
    for i in range(2,n+1):
        res = res*i%mod
        fac.append(res)
    return fac

# nの階乗の逆元のリスト
def fact_inv(n:int, inv:list, mod:int) -> list:
    facInv = [1,1]
    for i in range(2,n+1):
        facInv.append(facInv[i-1]*inv[i] % mod)
    return facInv
        
# 二項係数
def nCr(n:int, r:int, mod:int, fac:list, facInv:list) -> int:
    if not (0<=r and r<=n):
        return 0
    
    return ((fac[n]*facInv[r]) % mod) * facInv[n-r] % mod



MOD = 10**9+7
n = 2*10**5 + 1

H,W,A,B = map(int, input().split())

# 二項係数の準備
inv = inv_mod(n,MOD)
fac = fact(n,MOD)
facInv = fact_inv(n,inv,MOD)

# 手前×奥を実行して足していく
ans = 0
for h in range(H-A):
    temp = nCr(h+(B-1), h, MOD, fac, facInv) \
            * nCr((H-h-1)+(W-B-1), W-B-1, MOD, fac, facInv)
    ans = (ans + temp) % MOD
    
print(ans)