# ABC042D - いろはちゃんとマス目 / Iroha and a Grid (ARC058D)
def comb(n: int, r: int) -> int:
    return fact[n] * inv[n - r] * inv[r]


def main():
    global fact, inv
    H, W, A, B = tuple(map(int, input().split()))
    MOD = 10 ** 9 + 7
    # table of factorials
    fact, x = [1] * (H + W + 1), 1
    for i in range(1, H + W + 1):
        x = (x * i) % MOD
        fact[i] = x
    # table of inverse factorials
    inv = [1] * (H + W + 1)
    inv[-1] = pow(fact[-1], MOD - 2, MOD)
    x = inv[-1]
    for i in range(H + W - 1, 0, -1):
        x = (x * (i + 1)) % MOD
        inv[i] = x

    ans = 0
    for i in range(B, W):
        ans += comb(i + H - A - 1, i) * comb(W - i - 1 + A - 1, A - 1)
    print(ans % MOD)


if __name__ == "__main__":
    main()