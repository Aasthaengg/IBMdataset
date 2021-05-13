import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a = map(int, input().split())
    X = list(map(int, input().split()))
    MAX = 50 * 50 + 1

    dp = [[[0] * MAX for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1
    for i in range(1, n + 1):
        x = X[i - 1]
        for j in range(n):
            for k in range(MAX):
                dp[i][j][k] += dp[i - 1][j][k]
                if k + x < MAX:
                    dp[i][j + 1][k + x] += dp[i - 1][j][k]
    res = 0
    for j in range(1, n + 1):
        res += dp[-1][j][a * j]
    print(res)


if __name__ == '__main__':
    resolve()
