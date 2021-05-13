
#ABC042D
H, W, A, B = map(int, input().split())
mod=10**9+7
N=H+W+1
bikkuri=[0 for i in range(N)]
bikkuri[0]=1
for i in range(1,N):
    bikkuri[i] = (i * bikkuri[i-1])%mod
gyaku=[0 for i in range(N)]
gyaku[0]=1
for i in range(1, N):
    gyaku[i]=pow(bikkuri[i], mod-2, mod)
def comb(n,r):
    return bikkuri[n]*gyaku[n-r]*gyaku[r]%mod
def homb(n,r):
    return comb(n+r,r)%mod
dame = []
for i in range(B):
    dame.append(homb(H-A-1, i) * homb(W-1-i,A-1))
ans = homb(W-1, H-1) - sum(dame)
print(ans%mod)