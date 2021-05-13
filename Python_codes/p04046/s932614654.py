H, W, A, B = map(int, input().split())
mod = 10**9 + 7

fact = [1] * (H+W+1)
fact_inv = [1] * (H+W+1)
for i in range(1, H+W+1):
    fact[i] = i * fact[i-1] % mod
fact_inv[H+W] = pow(fact[H+W], mod-2, mod)
for i in range(1, H+W+1)[::-1]:
    fact_inv[i-1] = i * fact_inv[i] % mod
comb = lambda n, k: fact[n] * fact_inv[k] * fact_inv[n-k] % mod

ans = 0
for i in range(B+1, W+1):
    ans += comb((i-1) + (H-A-1), i-1) * comb((W-i) + (A-1), W-i) % mod
    ans %= mod
print(ans)
