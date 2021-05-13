U = 2*10**5
MOD = 10**9+7
 
fact = [1] * (U+1)
fact_inv = [1] * (U+1)

# 階乗のテーブル作成
for i in range(1, U+1):
    fact[i] = (fact[i-1] * i) % MOD

# 階乗の逆元のテーブル作成
fact_inv[U] = pow(fact[U], MOD-2, MOD)
for i in range(U, 0, -1):
    fact_inv[i-1] = (fact_inv[i] * i) % MOD

def comb(n, k):
    if k < 0 or k > n:
        return 0
    x = fact[n]
    x *= fact_inv[k]
    x %= MOD
    x *= fact_inv[n-k]
    x %= MOD
    return x

H, W, A, B = [int(i) for i in input().split(" ")]

ans = 0
# 経路の足し上げ C(縦+横, 縦(or横)) (重複のある組み合わせ)
for i in range(B, W):
    ans += comb((H-A-1) + i, i) * comb((A - 1) + (W-1-i), W-1- i) % MOD
    ans %= MOD
print(ans)