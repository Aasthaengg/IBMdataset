import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, A, *X = map(int, read().split())

    M = sum(X)
    dp = [[0] * (M + 1) for j in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N, 0, -1):
            for k in range(X[i], M + 1):
                dp[j][k] += dp[j - 1][k - X[i]]

    ans = 0
    for j in range(1, min(N, M // A) + 1):
        ans += dp[j][A * j]

    print(ans)
    return


if __name__ == '__main__':
    main()
