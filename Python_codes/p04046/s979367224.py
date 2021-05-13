h,w,a,b=map(int,input().split())
mod=pow(10,9)+7

# コンビネーション、さらに高速。あらかじめO(N)の計算をすることでのちの計算が早くなる
def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
g1 = [1, 1] 
g2 = [1, 1] 
inverse = [0, 1]
for i in range( 2, 200000 + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )
ans=0
for k in range(1,h-a+1):
  tmp=cmb(k-1+b-1,k-1,mod)
  tmp*=cmb(h-k+w-b-1,h-k,mod)
  ans+=tmp
  ans%=mod
print(ans)