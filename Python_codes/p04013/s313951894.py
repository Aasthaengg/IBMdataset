import numpy as np
import sys
input = sys.stdin.readline

def main():
    N, A = map(int, input().split())
    x = np.array(list(map(int, input().split())))
    X = max(A, max(x))
    x -= A
    # print(x)
    dp = np.zeros((N+1, 2*N*X+1), dtype=int)
    # 初期化
    dp[0][N*X] = 1
    for i in range(N):
        dp[i+1] += dp[i]
        if x[i] > 0:
            dp[i+1][x[i]:] += dp[i][:-x[i]]
        elif x[i] < 0:
            dp[i+1][:x[i]] += dp[i][-x[i]:]
        else:
            dp[i+1] += dp[i]
    
    # print(dp[:, N*X-5:N*X+5])
    # print(x)
    print(dp[-1][N*X] - 1)

if __name__ == "__main__":
    main()