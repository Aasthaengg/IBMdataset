h,w,a,b=map(int,input().split())
mod=10**9+7
fact=[1]*(h+w+1)
for i in range(1,h+w+1):
    fact[i]=(fact[i-1]*i)%mod
def cmb(a,b):
    return fact[a]*pow(fact[b],mod-2,mod)*pow(fact[a-b],mod-2,mod)%mod
ans=0
for i in range(b,w):
    ans+=cmb(h-a+i-1,i)*cmb(w-1-i+a-1,w-i-1)%mod
print(ans%mod)
