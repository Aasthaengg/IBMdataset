import sys
input = sys.stdin.readline


def main():
    n, a = map(int, input().split())
    x = tuple(map(int, input().split()))

    sm_mx = sum(x)

    dp = [[[0] * (sm_mx + 1) for _ in range(n + 1)] for _ in range(n + 1)]

    dp[0][0][0] = 1

    for i, e in enumerate(x, 1):
        for j in range(n + 1):
            for sm in range(sum(x[:i]) + 1):
                if sm < e:
                    dp[i][j][sm] = dp[i-1][j][sm]
                elif j >= 1 and sm >= e:
                    dp[i][j][sm] = dp[i-1][j][sm] + dp[i-1][j-1][sm-e]

    ans = 0
    for i in range(1, n + 1):
        if i > sm_mx / a:
            break
        ans += dp[n][i][i*a]

    print(ans)


if __name__ == "__main__":
    main()
