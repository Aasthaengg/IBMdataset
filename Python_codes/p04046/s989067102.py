h,w,a,b=map(int,input().split())
N=h+w
mod=10**9+7
fac=[1]*(N+2)
inv=[1]*(N+2)
t=1
for i in range(1,N+2):
    t*=i
    t%=mod
    fac[i]=t
t=pow(fac[N+1],mod-2,mod)
for i in range(N+1,0,-1):
    inv[i]=t
    t*=i
    t%=mod
def comb(n,r):
    return fac[n]*inv[n-r]*inv[r]%mod
c=[0]
for i in range(h-a):
    c.append(comb(b+i,i))
ans=0
for i in range(h-a):
    ans+=(c[i+1]-c[i])*comb(w-b+h-i-2,w-b-1)%mod
    ans%=mod
print(ans)