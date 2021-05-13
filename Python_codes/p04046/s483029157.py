H,W,A,B = map(int,input().split())
N=H+W
fact = [0]*(N+1)
ifact = [0]*(N+1)
inv = [0]*(N+1)
p=10**9+7

def combination(n):
    fact[0] = 1
    fact[1] = 1
    ifact[0] = 1
    ifact[1] = 1
    inv[1] = 1
    for i in range(2,n+1):
        fact[i] = (fact[i-1]*i)%p
        inv[i] = p - inv[p%i]*(p//i)%p
        ifact[i] = (ifact[i-1]*inv[i])%p
def op(n,k):
    if k<0 or k>n or n<0:
        return 0
    return (fact[n]*ifact[k]*ifact[n-k])%p
combination(N)

b = op(H-A+B-1, B)
res = 0
for i in range(A):
    res = (res + op(W-B-2+i, i))%p
res = (res*b)%p
for i in range(H-A):
    res = (res + op(B+i, i)*op(H-i-1+W-B-2,W-B-2))%p
if H-A==1 and W-B==1:
    res = 1
elif H-A==1:
    res = op(W-B+H-2, H-1)
elif W-B==1:
    res = op(H-A+W-2, W-1)
print(res)