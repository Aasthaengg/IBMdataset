H, W, A, B = map(int, input().split())

MOD = 10 ** 9 + 7


def pow_mod(x, p):
    res = 1
    while p:
        if p % 2:
            res = res * x % MOD
        x = x * x % MOD
        p //= 2
    return res


F = [1]
invF = []


def comb_mod(n, r):
    return F[n] * invF[r] * invF[n - r] % MOD


for i in range(1, H + W - 1):
    F.append(F[-1] * i % MOD)

invF.append(pow_mod(F[-1], (MOD - 2)))
for f in range(len(F) - 1):
    invF.append(invF[-1] * (len(F) - len(invF)) % MOD)
invF = invF[::-1]

res = 0
for i in range(B + 1, W + 1):
    p = H - A - 1
    q = i - 1

    res = (
                  res
                  + comb_mod(H - A - 1 + i - 1, H - A - 1)
                  * comb_mod(A - 1 + W - i, W - i)
          ) % MOD

print(res)
