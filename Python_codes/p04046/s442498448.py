H, W, A, B = map(int, input().split())

ans = 0 
MOD = 10**9 + 7
N = H + W - 2
fac = [1] * (N+1)
inv = [1] * (N+1)

# 階乗
for i in range(1, N+1):
    fac[i] = i * fac[i - 1] % MOD
 
# 普通の逆元テーブル
for i in range(1, N+1):
    inv[i] = pow(fac[i], MOD-2, MOD)
 
 
def f(x, y):
    ans = fac[x + y] * inv[x] * inv[y] % MOD
    return ans
 

for x in range(B, W):
    ans += f(x, H - A - 1) * f(W - 1 - x, A - 1)
    ans %= MOD
    
print(ans % MOD)