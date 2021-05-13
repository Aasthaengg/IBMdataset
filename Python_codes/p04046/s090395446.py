H, W, A, B = map(int, input().split())

ans = 0 
MOD = 10**9 + 7
N = H + W - 2
fac = [1] * N
inv = [1] * N

# 階乗
for i in range(1, N):
    fac[i] = (fac[i - 1] * i) % MOD
 
# 高速な逆元テーブル　最初にN-1を求めておくことであとはiをかけるだけで残りの逆元が算出できる
inv[N - 1] = pow(fac[N - 1], MOD - 2, MOD)
for i in range(N - 1, 0, -1):
    inv[i - 1] = (inv[i] * i) % MOD
 
 
def f(x, y):
    ans = fac[x + y] * inv[x] * inv[y] % MOD
    return ans
 

for x in range(B, W):
    ans += f(x, H - A - 1) * f(W - 1 - x, A - 1)
    ans %= MOD
    
print(ans % MOD)