import sys
input = sys.stdin.readline
H,W,A,B= map(int,input().split())

MOD = 10**9 + 7
num = 200010
fact = [1] * (num+1)
ifact = [1] * (num+1)

for i in range(1,num+1):
    fact[i] = (fact[i-1] * i) % MOD
ifact[-1] = pow(fact[-1],MOD-2,MOD)
for i in range(1,num+1)[::-1]:
    ifact[i-1] = (ifact[i] * i)% MOD

def nCr(n,r):
    if r > n:
        return 0
    return (fact[n] * ifact[r] * ifact[n-r]) % MOD

ans = 0
for i in range(B+1,W+1):
    ans += nCr((i-1)+(H-A-1),i-1) * nCr((A-1)+(W-i),A-1)
    ans %= MOD
print(ans)
