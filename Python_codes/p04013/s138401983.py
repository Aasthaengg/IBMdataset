import sys
input = sys.stdin.readline

def main():
    N, A = (int(_) for _ in input().split())
    X = [int(_) for _ in input().split()]

    dp = [[[0] * (N*A+1) for _ in range(N+1)] for __ in range(N+1)]

    dp[0][0][0] = 1
    for i in range(N):
        for j in range(N):
            for k in range(N*A+1):
                dp[i+1][j][k] += dp[i][j][k]
                if k - X[i] >= 0:
                    dp[i+1][j+1][k] += dp[i][j][k-X[i]]
    ret = 0
    for i in range(1, N+1):
        ret += dp[N][i][i*A]
    print(ret)
    return

if __name__ == '__main__':
    main()
