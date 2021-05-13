# coding: utf-8
# Your code here!
h,w,a,b=map(int,input().split())
MOD=10**9+7
fac=[0]*2*10**5
finv=[0]*2*10**5
inv=[0]*2*10**5
fac[0]=fac[1]=1
finv[0]=finv[1]=1
inv[1]=1
for i in range(2,2*10**5):
    fac[i]=(fac[i-1]*i)%MOD
    inv[i]=MOD-inv[MOD%i]*(MOD//i)%MOD
    finv[i]=finv[i-1]*inv[i]%MOD
def COM(n,k):
    if n<k:
        return 0
    if n<0 or k<0:
        return 0
    return fac[n]*(finv[k]*finv[n-k]%MOD)%MOD
ans=0
for i in range(b,w):   
    ans+=COM(h-a-1+i,i)*COM(a-1+w-i-1,w-i-1)
    ans=ans%MOD
print(ans)