h,w,a,b=map(int,input().split())
mod=10**9+7

n=h+w+1
fc,inv=[1]*n,[1]*n
for i in range(1,n):
    fc[i]=i*fc[i-1]%mod
inv[n-1]=pow(fc[n-1],mod-2,mod)
for i in range(n-1,0,-1):
    inv[i-1]=inv[i]*i%mod
f=lambda a,b:fc[a+b]*inv[a]*inv[b]%mod

v=0
for i in range(b,w):
    v+=f(h-a-1,i)*f(a-1,w-i-1)%mod
print(v%mod)
