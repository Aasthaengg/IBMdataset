H,W,A,B=map(int,input().split())
N=H+W
mod=10**9+7
factl=[1]
for i in range(1,N+1):
    factl.append(factl[-1]*i%mod)
invl=[pow(factl[-1],mod-2,mod)]
for i in range(N,0,-1):
    invl.append(invl[-1]*i%mod)
invl.reverse()
def Comb(a,b):
    return factl[a]*invl[a-b]*invl[b]
ans=0
for i in range(H-A):
    ans+=Comb(B+i-1,i)*Comb((W-B-1)+(H-i-1), H-i-1)
    ans%=mod
print(ans)