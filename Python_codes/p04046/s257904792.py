H, W, A, B = map(int,input().split())
MOD = 10**9 + 7
def prepare(n, MOD):

    # 1! - n! の計算
    f = 1
    factorials = [1]  # 0!の分
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    # n!^-1 の計算
    inv = pow(f, MOD - 2, MOD)
    # n!^-1 - 1!^-1 の計算
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv

    return factorials, invs

factorials, invs = prepare(H+W+1,MOD)
ans = 0
for b in range(B,W):
  ans += (factorials[H-A-1+b] * invs[H-A-1] % MOD * invs[b] % MOD) * (factorials[A-1+W-b-1] * invs[A-1] % MOD * invs[W-b-1] % MOD)
print(ans % MOD)