def inpl(): return list(map(int, input().split()))
H, W, A, B = inpl()

MOD = 10**9 + 7
def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
 
size = H+ W + 1
g1, g2, inverse = [0]*size, [0]*size, [0]*size
 
g1[:2] = [1, 1] # 元テーブル
g2[:2] = [1, 1] #逆元テーブル
inverse[:2] = [0, 1] #逆元テーブル計算用テーブル
 
for i in range(2, size):
    g1[i] =  ( g1[i-1] * i ) % MOD 
    inverse[i] = (-inverse[MOD % i] * (MOD//i) ) % MOD 
    g2[i] =  (g2[i-1] * inverse[i]) % MOD

ans = 0
for a in range(H-A):
    h = H - a - 1
    w = W - B - 1
    ans = (ans + cmb(a+B-1, a, MOD)*cmb(h+w, h, MOD))%MOD
print(ans)