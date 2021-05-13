import sys
input = sys.stdin.buffer.readline

def main():
    N,A = map(int,input().split())
    x = list(map(int,input().split()))
    S = sum(x)
    
    dp = [[[0 for _ in range(S+1)] for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(N):
            for k in range(S):
                if dp[i][j][k] == 0:
                    continue
                dp[i+1][j][k] += dp[i][j][k]
                dp[i+1][j+1][k+x[i]] += dp[i][j][k]

    M = S//A
    ans = 0
    for i in range(1,N+1):
        if i*A <= S:
            ans += dp[-1][i][i*A]
    
    print(ans)
    
if __name__ == "__main__":
    main()