import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

MOD = 10**9+7
fac = [1, 1]
f_inv = [1, 1]
inv = [0, 1]

def modcmb(n, r, mod):
    if n < 0 or r < 0 or r > n:
        return 0

    return fac[n] * f_inv[r] * f_inv[n-r] % mod


def main():
    H,W,A,B = map(int, readline().split())

    n = H+W+1
    for i in range(2,n):
        fac.append((fac[-1] * i) % MOD)
        inv.append((-inv[MOD % i] * (MOD//i)) % MOD)
        f_inv.append((f_inv[-1] * inv[-1]) % MOD)

    ans = 0
    for i in range(H-A):
        ans += modcmb(B-1+i, B-1, MOD) * modcmb(H+W-B-2-i, W-1-B, MOD) % MOD
        ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
