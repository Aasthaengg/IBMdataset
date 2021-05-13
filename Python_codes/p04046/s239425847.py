H,W,A,B=map(int,input().split())
N=H+W+2
mod=10**9+7
table=[1]*(N+3)
t=1
for i in range(1,N+3):
    t*=i
    t%=mod
    table[i]=t
rtable=[1]*(N+3)
t=1
for i in range(1,N+3):
    t*=pow(i,mod-2,mod)
    t%=mod
    rtable[i]=t
ans=0
for i in range(H-A):
    t=table[B-1+i]*rtable[i]*rtable[B-1]
    s=table[W+H-B-i-2]*rtable[H-i-1]*rtable[W-B-1]
    t=(t*s)%mod
    #print(t)
    ans+=t
    ans%=mod
print(ans)