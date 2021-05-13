h,w,a,b = map(int,input().split())
mod = 10 ** 9 + 7

def inv(a,mod):
    r = [1,0,a]
    w = [0,1,mod]
    while w[2]!=1:
        q = r[2]//w[2]
        r_new = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = w
        w = r_new
    x,y = w[0],w[1]    # a*x+y*mod = 1
    return (mod+x%mod)%mod

max_num = 2*10**5+1
fact = [0 for _ in range(max_num)]
ifact = [0 for _ in range(max_num)]

fact[0] = fact[1] = 1
ifact[0] = ifact[1] = 1

for i in range(2,max_num):
    fact[i] = fact[i-1] * i % mod
    ifact[i] = ifact[i-1] * inv(i,mod) % mod

def cmb(x,y):
    return fact[x] * ifact[y] * ifact[x-y] % mod

ans = 0

j = 0
while j < min(w-b,h-a):
    ans += cmb(b+h-a-1,b+j)*cmb(a+w-b-1,a+j)
    ans %= mod
    j += 1

print(ans)