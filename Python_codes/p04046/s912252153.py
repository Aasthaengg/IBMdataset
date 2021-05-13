h,w,a,b = map(int,input().split())
n = h+w
mod = 10**9+7
fun = [1]*(n+1)
for i in range(1,n+1):
    fun[i] = fun[i-1]*i%mod
rev = [1]*(n+1)
rev[n] = pow(fun[n],mod-2,mod)
for i in range(n-1,0,-1):
    rev[i] = rev[i+1]*(i+1)%mod
def nCr(n,r):
    if r > n:
        return 0
    return fun[n]*rev[r]%mod*rev[n-r]%mod
ans = 0
i = h-a
j = b+1
while i > 0 and j <= w:
  ans = (ans+nCr(i+j-2,i-1)*nCr(h+w-i-j,h-i)%mod)%mod
  i -= 1
  j += 1
print(ans)
