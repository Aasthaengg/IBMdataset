import numpy as np


def main(n, a, x):
    SUM_MAX = max(a, max(x)) * n + 1
    dp = np.zeros(shape=(n + 1, n + 1, SUM_MAX), dtype=int)

    dp[0][0][0] = 1
    for j in range(1, n + 1):
        for k in range(j + 1):
            dp[j][k][0:x[j - 1]] = dp[j - 1][k][0:x[j - 1]]
            if k >= 1:
                dp[j][k][x[j - 1]:] = dp[j - 1][k][x[j - 1]:] + dp[j - 1][k - 1][:SUM_MAX - x[j - 1]]

    patterns = 0
    for k in range(1, n + 1):
        ka = k * a
        patterns += dp[n][k][ka]
    return patterns


if __name__ == '__main__':
    N, A = map(int, input().split())
    X = list(map(int, input().split()))
    print(main(N, A, X))
