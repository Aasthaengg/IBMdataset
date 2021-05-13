H,W,A,B = map(int,input().split())
mod = 10**9+7
x1 = [1 for i in range(H+W)]
xi = [1 for i in range(H+W)]
num = 1
def power2(a,b,p):
    if b == 0:
        return 1
    if b%2 == 0:
        d = power2(a,b//2,p)
        return (d*d)%p
    return (a*power2(a,b-1,p))%p
for i in range(1,H+W):
    num = (num*i)%mod
    x1[i] = num
for i in range(1,H+W):
    x2 = power2(x1[i],mod-2,mod)
    xi[i] = x2
def comb(a,b,p):
    return (x1[a]*xi[b]*xi[a-b])%p
ans = 0
for w in range(B,W):
    ans = (ans+ (comb(H-A+w-1,w,mod)*comb(A+W-w-2,A-1,mod))%mod)%mod
print(ans)