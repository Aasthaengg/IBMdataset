mod=10**9+7
h,w,a,b=map(int,input().split())
F,I=[0]*(h+w+2),[0]*(h+w+2)
def inv(n):
  return pow(n,mod-2,mod)
F[0],F[1],I[0],I[1]=1,1,1,1
for i in range(2,h+w+2):
  F[i]=i*F[i-1]%mod
  I[i]=inv(F[i])
def c(a,b):
  return F[a+b]*I[a]*I[b]%mod
ans=0
for i in range(b+1,w+1):
  ans+=(c(h-a-1,i-1)*c(a-1,w-i))%mod
print(ans%mod)