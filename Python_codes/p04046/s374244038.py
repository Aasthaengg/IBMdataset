mod = 10 ** 9 + 7

H, W, A, B = map(int, input().split())

fact = [-1] * (H + W + 1)
fact[0] = 1
fact[1] = 1
for x in range(2, H + W + 1):
    fact[x] = x * fact[x - 1] % mod

invs = [-1] * (H + W + 1)
invs[H + W] = pow(fact[H + W], mod - 2, mod)
for x in range(H + W - 1, 0, -1):
    invs[x] = invs[x + 1] * (x + 1) % mod


def combination(n, r):
    if n - r < r:
        return combination(n, n - r)
    if r < 0:
        return 0
    if r == 0:
        return 1
    if r == 1:
        return n
    return fact[n] * invs[r] * invs[n - r] % mod


ret = 0
for c in range(B, W):
    ret = (ret + combination(H - 1 - A + c, c) * combination(W - 2 + A - c, A - 1)) % mod
print(ret)

# 左下にA*Bの入れない区画
# S->{aa,bb,cc,dd,ee,ff,gg}->G
# S->aはcombination(H - 1 - A + c, c):aの座標(H-1-A,c),通る列番号cを選ぶ
# a->aは1通り
# a->Gはcombination(W - 2 + A - c, A - 1):aの座標(H-A,c),Gの座標(H-1,W-1)この距離からA-1を選ぶ
# S**********
# *         *
# *         *
# *         *
# ****abcdefg
# *   abcdefg
# *   *     *
# *   *     *
# **********G