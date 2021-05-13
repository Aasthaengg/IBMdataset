n=200000
mod=10**9+7
def pf(x,y,p):
  if y==0: return 1
  if y%2==0:
    d=pf(x,y//2,p)
    return d*d%p
  if y%2==1:
    return (x*pf(x,y-1,p))%p
facl=[1]
for i in range(1,n+2):
  facl.append(facl[i-1]*i%mod)
invl=[1]*(n+2)
for i in range(1,n+2):
  invl[i]=pf(facl[i],mod-2,mod)
def comb(x,k):
  if x<0 or k<0 or x<k: return 0
  if x==0 or k==0: return 1
  return (facl[x]*invl[k]*invl[x-k])%mod
h,w,a,b=map(int,input().split())
if h-a<w-b:
  h,w=w,h
  a,b=b,a
t=0
for i in range(w-b):
  t+=comb(h-a+b-1,b+i)*comb(w-b+a-1,a+i)
print(t%mod)