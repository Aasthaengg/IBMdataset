def main():
    n, a = map(int, input().split())
    x = list(map(int, input().split()))

    mx = max(x + [a])

    for i in range(n):
        x[i] -= a

    sm = 2 * n * mx

    dp = [[0] * (sm + 1) for _ in range(n + 1)]

    dp[0][n*mx] = 1

    for i, e in enumerate(x, 1):
        for j in range(sm + 1):
            if 0 <= j - e <= sm:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-e]
            else:
                dp[i][j] = dp[i-1][j]

    ans = dp[n][n*mx] - 1

    print(ans)


if __name__ == "__main__":
    main()
