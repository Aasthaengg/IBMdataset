def main():
    H, W, A, B = map(int, input().split())
    mod = 10**9 + 7
    ans = 0

    # 予め階乗を計算しておく
    f = [1]
    for i in range(H+W):
        f.append(f[i]*(i+1)%mod)

    # 組み合わせ関数
    def comb_mod(n, r, p):
        return f[n] * pow(f[r], p-2, p) * pow(f[n-r], p-2, p)

    for i in range(H-A):
        ans += comb_mod(i+B-1,B-1,mod) * comb_mod(H-1-i+W-B-1,W-B-1,mod)

    print(ans%mod)

if __name__ == '__main__':
    main()