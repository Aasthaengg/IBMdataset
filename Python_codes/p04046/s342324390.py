mod=10**9+7
g1=[1,1]
g2=[1,1]
inverse=[0,1]
h,w,a,b=map(int,input().split())
n=h+w
for i in range(2,n+1):
    g1.append((g1[-1]*i)%mod)
    inverse.append((-inverse[mod % i]*(mod//i))%mod)
    g2.append((g2[-1]*inverse[-1])%mod)
def cmb(n,r):
    return g1[n]*g2[r]*g2[n-r]%mod
 
ans=0
while a<h and b<w:
    ans=(ans+cmb(h-1-a+b,b)*cmb(w-1-b+a,a))%mod
    a+=1
    b+=1
print(ans)