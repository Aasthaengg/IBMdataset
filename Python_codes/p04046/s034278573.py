import sys


def comb(n, r, MOD, factrial, fact_inv):
    if n < 0 or r < 0 or n < r:
        return 0
    else:
        return (factrial[n] * fact_inv[r] * fact_inv[n-r]) % MOD

def main():
    input = sys.stdin.readline
    H, W, A, B = map(int, input().split())
    MOD = 10**9 + 7

    n = H + W - 2

    factrial = [1] * (n+1)
    for k in range(1, n+1):
        factrial[k] = (factrial[k-1] * k) % MOD

    fact_inv = [1] * (n+1)
    fact_inv[n] = pow(factrial[n], MOD - 2, MOD)
    for k in range(n-1, -1, -1):
        fact_inv[k] = (fact_inv[k+1] * (k+1)) % MOD
    

    ans = 0
    for w in range(B+1, W+1):
        n_a = H - A + w -2
        r_a = w - 1
        a = comb(n_a, r_a, MOD, factrial, fact_inv)

        n_b = A - 1 + W - w
        r_b = A - 1
        b = comb(n_b, r_b, MOD, factrial, fact_inv)

        ans += (a * b) % MOD

    return ans % MOD


if __name__ == '__main__':
    print(main())
