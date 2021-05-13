MOD = 10**9 + 7
MAX = int(2e5+1)


def div(a, b):
    return a * pow(b, MOD-2, MOD) % MOD


FACT = [1] * (MAX+1)
for i in range(1, MAX+1):
    FACT[i] = (i * FACT[i-1]) % MOD
INV = [1] * (MAX+1)
INV[MAX] = div(1, FACT[MAX])
for i in range(MAX, 0, -1):
    INV[i-1] = (INV[i] * i) % MOD


def main():
    H, W, A, B = map(int, input().split())
    ans = 0
    i = H-A-1
    j = B
    while i >= 0 and j < W:
        a = (FACT[i+j] * INV[i] * INV[j]) % MOD
        b = (FACT[H-i-1 + W-j-1] * INV[H-i-1] * INV[W-j-1]) % MOD
        ans = (ans + a * b) % MOD
        i -= 1
        j += 1
    print(ans)


if __name__ == "__main__":
    main()
