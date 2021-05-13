H,W,A,B = map(int,input().split())
P=10**9+7
fac=[1]*(H+W)
inv=[1]*(H+W)
finv=[1]*(H+W)
for n in range(2,H+W):
    fac[n]=fac[n-1]*n%P
    inv[n]=(-inv[P%n]*(P//n))%P
    finv[n]=finv[n-1]*inv[n]%P
def comb(n,k):return ((fac[n]*finv[k]%P)*finv[n-k])%P
ans=0
for i in range(1,min(W-B+1,H-A+1)):
    w=B+i-1
    h=H-A-i
    ans=(ans+comb(w+h,w)*comb(W+H-w-h-2,W-w-1))%P
print(ans)