H, W, A, B = map(int, input().split())
ans = 0

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = maximum = max(H - A + W - 2, W + A - B - 2)
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

for i in range(W - B):
    #前半の経路
    P = 10 ** 9 + 7
    prev = cmb(H - A + B - 1 + i, H - A - 1, P) % P
    latter = cmb(A - 1 + W - B - 1 - i, A - 1, P) % P
    ans += (prev * latter) % P
    ans = ans % P
print(ans)




