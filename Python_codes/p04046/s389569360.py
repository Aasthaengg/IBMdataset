import sys
input=sys.stdin.readline

mod = 10**9+7
def nCr(fact, inv, n, r):
    return fact[n] * inv[r] * inv[n-r] % mod

def main():
    H,W,A,B = map(int,input().split())
    fact = [1]
    for i in range(1, H+W+1):
        fact.append(fact[i-1] * i % mod)
    
    inv = [0] * (H+W+1)
    inv[H+W] = pow(fact[H+W], mod-2, mod) # フェルマーの小定理より a**(mod-2)はaの逆元
    for i in range(H+W, 0, -1):
        inv[i-1] = inv[i] * i % mod

    ans = 0
    for i in range(W-B):
        n0 = H-A-1+B+i
        r0 = H-A-1
        n1 = A-1+W-B-1-i
        r1 = A-1
        ans += nCr(fact, inv, n0, r0) * nCr(fact, inv, n1, r1) % mod
    print(ans%mod)

if __name__ == '__main__':
    main()
