mod = 10**9+7
mod2 = 998244353
rng = 200001
fctr = [1]
finv = [1]
for i in range(1,rng):
    fctr.append(fctr[-1]*i%mod)
for i in range(1,rng):
    finv.append(pow(fctr[i],mod-2,mod))
def cmb(n,k):
    if n<0 or k<0:
        return 0
    else:
        return fctr[n]*finv[n-k]*finv[k]%mod
h,w,a,b = map(int, input().split(' '))
ans = cmb(h+w-2,h-1)
x = h-a+b-1
for i in range(1,min(a,b)+1):
    ans = (ans-(cmb(x,b-i)*cmb(h+w-2-x,w-b+i-1))%mod)%mod
print(ans)