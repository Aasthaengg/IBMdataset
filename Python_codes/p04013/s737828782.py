def main():
    N, A = (int(i) for i in input().split())
    X = [int(i) for i in input().split()]
    dp = [[[0 for s in range(N*A + 1)] for k in range(N + 1)]
          for j in range(N + 1)]
    dp[0][0][0] = 1
    for j in range(1, N+1):
        for k in range(0, N+1):
            for s in range(N*A + 1):
                dp[j][k][s] = dp[j-1][k][s]
                if k >= 1 and s - X[j-1] >= 0:
                    dp[j][k][s] += dp[j-1][k-1][s-X[j-1]]
    ans = 0
    for k in range(1, N+1):
        ans += dp[N][k][k*A]
    print(ans)


if __name__ == '__main__':
    main()
