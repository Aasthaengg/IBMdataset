H,W,A,B = map(int, input().split())
MOD = 10 ** 9 + 7

N = H+W+1

def power(base, num):
    if num == 0:
        return 1
    elif num % 2==0:
        return power(base, num//2) **2 % MOD
    elif num==1:
        return base % MOD
    else:
        return power(base, num//2) **2 * base % MOD

fact = [0 for i in range(N)]
inv_fact = [0 for i in range(N)]

fact[0] = 1
for i in range(1, N):
    fact[i] = fact[i-1] * i % MOD
    
inv_fact[H+W] = power(fact[H+W], MOD-2)
for i in range(1, N):
    inv_fact[N-1-i] = inv_fact[N-i] * (N-i) % MOD

    
def comb(x,y):
    return (fact[x] * inv_fact[y])%MOD * inv_fact[x-y] % MOD

ans = 0

for i in range(1, W-B+1):
    ans += comb(H-A+B-2+i, H-A-1) * comb(A-1+W-B-i, A-1) % MOD
    ans %= MOD
print(ans%MOD)
