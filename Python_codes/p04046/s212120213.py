import sys
h, w, a, b = [int(i) for i in sys.stdin.readline().split()]
dic = dict()
MOD = 10**9+7

def nCr(n, r, mod=MOD):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 10**6
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )



res = 0
_sum = 0
for i in range(h - a):
    dic[i] = nCr(i + b, i)
    res += (dic[i] - _sum) * nCr(h - i - 1 + w - b - 1, h - i - 1)
    _sum = dic[i]
    res %= MOD
print(res)