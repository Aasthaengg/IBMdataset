MAX = 2*10**5+100
fact = [0]*MAX
inv = [0]*MAX
finv = [0]*MAX
 
def C_init():
    fact[0] = 1
    fact[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1
    
    for i in range(2, MAX):
        fact[i] = fact[i-1]*i%MOD
        inv[i] = MOD-inv[MOD%i]*(MOD//i)%MOD
        finv[i] = finv[i-1]*inv[i]%MOD
 
def C(n, r):
    if n<r:
        return 0
    if n<0 or r<0:
        return 0
    return fact[n]*(finv[r]*finv[n-r]%MOD)%MOD

H, W, A, B = map(int, input().split())
MOD = 10**9+7
C_init()
ans = 0

for i in range(H-A):
    ans += C(i+B-1, i)*C(H-1-i+W-B-1, W-B-1)
    ans %= MOD

print(ans)