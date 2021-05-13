import numpy as np


def main(n, a, x):
    X = max(a, max(x))
    NX = X * n
    NX2 = 2 * NX
    dp = np.zeros(shape=(n + 1, NX2 + 1), dtype=int)
    dp[0][NX] = 1
    for j in range(1, len(dp)):
        for t in range(len(dp[j])):
            xj = x[j - 1]
            yj = xj - a
            if 0 <= t - yj <= NX2:
                dp[j][t] = dp[j - 1][t] + dp[j - 1][t - yj]
            else:
                dp[j][t] = dp[j - 1][t]
    return dp[n][NX] - 1


if __name__ == '__main__':
    N, A = map(int, input().split())
    X = list(map(int, input().split()))
    print(main(N, A, X))
