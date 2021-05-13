import sys
input = sys.stdin.readline

def main():
    H, W, A, B = map(int, input().split())

    MOD = int(1e9) + 7

    kai = [1] * (max(H-A+W, A+W-B) + 1)
    for i in range(1, len(kai)):
        kai[i] = kai[i-1] * i
        kai[i] %= MOD
    
    up = [0] * (W-B)
    down = [0] * (W-B)

    t1 = H-A-1
    for i in range(W-B):
        t2 = B + 1 + i-1
        # print(t1, t2)
        up[i] = kai[t1 + t2] * pow(kai[t1], MOD-2, MOD) * pow(kai[t2], MOD-2, MOD)
        up[i] %= MOD
    t1 = A-1
    for i in range(W-B):
        t2 = W-B-i-1
        # print(t1, t2)
        down[i] = kai[t1 + t2] * pow(kai[t1], MOD-2, MOD) * pow(kai[t2], MOD-2, MOD)
        down[i] %= MOD
    
    ans = 0
    for i in range(W-B):
        ans += (up[i] * down[i])
        ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()