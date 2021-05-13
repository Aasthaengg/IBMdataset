import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, A, *X = map(int, read().split())

    X = [x - A for x in X]
    base = 2500
    dp = [[0] * 5001 for _ in range(N + 1)]
    dp[0][base] = 1

    for i in range(N):
        for s in range(5001):
            dp[i + 1][s] = dp[i][s]
            if 0 <= s - X[i] <= 5000:
                dp[i + 1][s] += dp[i][s - X[i]]

    print(dp[N][base] - 1)
    return


if __name__ == '__main__':
    main()
