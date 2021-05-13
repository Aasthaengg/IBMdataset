import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, A, *X = map(int, read().split())

    dp = [[0] * (N * 50 + 1) for j in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N, -1, -1):
            for k in range(N * 50 + 1):
                if k - X[i] >= 0 and j > 0:
                    dp[j][k] += dp[j - 1][k - X[i]]

    ans = 0
    for j in range(1, N + 1):
        ans += dp[j][A * j]

    print(ans)
    return


if __name__ == '__main__':
    main()
