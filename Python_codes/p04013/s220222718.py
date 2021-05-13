import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 998244353


def resolve():
    n, a = map(int, input().split())
    X = list(map(int, input().split()))
    MAX = sum(X)
    dp = [[[0] * (MAX + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1
    for i in range(1, n + 1):
        x = X[i - 1]
        for j in range(n + 1):
            for k in range(MAX + 1):
                dp[i][j][k] += dp[i - 1][j][k]
                if k + x < MAX + 1 and j + 1 <= n:
                    dp[i][j + 1][k + x] += dp[i - 1][j][k]
    res = 0
    for j in range(1, n + 1):
        total = a * j
        if total <= MAX:
            res += dp[n][j][total]
    print(res)


if __name__ == '__main__':
    resolve()
