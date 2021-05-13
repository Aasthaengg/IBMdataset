H, W, A, B = map(int, input().split())
MOD = 10 ** 9 + 7

# 階乗 & 逆元計算
factorial = [1]
inverse = [1]
for i in range(1, H + W + 2):
    factorial.append(factorial[-1] * i % MOD)
    inverse.append(pow(factorial[-1], MOD - 2, MOD))


# 組み合わせ計算
def nCr(n, r):
    if n < r or r < 0:
        return 0
    elif r == 0:
        return 1
    return factorial[n] * inverse[r] * inverse[n - r] % MOD


ans = 0
for w in range(B, W):
    ans += nCr(H - A - 1 + w, w) * nCr(A - 1 + W - w - 1, A - 1) % MOD
    ans %= MOD
print(ans % MOD)
