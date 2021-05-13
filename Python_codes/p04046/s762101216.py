#cmb
mod=10**9+7
MAX=2*10**5+100

g1=[1,1]
g2=[1,1]
for i in range(2,MAX+1):
    num_1=g1[-1]*i%mod
    g1.append(num_1)
    g2.append(pow(num_1,mod-2,mod))
    
def cmb(n,r,MOD):
    return g1[n]*g2[r]*g2[n-r]%MOD

h,w,a,b=map(int,input().split())
ans=0
for i in range(1,h-a+1):
    ans=(ans+cmb(i+b-2,i-1,mod)*cmb(h-i+w-b-1,h-i,mod))%mod

print(ans)