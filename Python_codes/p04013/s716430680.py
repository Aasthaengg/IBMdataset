def main():
    n,a = map(int,input().split())
    x = [int(x) for x in input().split()]
    dp= [[[0 for _ in range(2501)] for _ in range(n+1)] for _ in range(n)]

    dp[0][0][0] = 1
    dp[0][1][x[0]] = 1

    for i in range(1,n):
        for j in range(n+1):
            for k in range(2501):
                if k<x[i]:
                    dp[i][j][k] = dp[i-1][j][k]
                else:
                    dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k-x[i]]
    ans = 0
    for i in range(1,n+1):
        ans += dp[-1][i][a*i]
    print(ans)
    
if __name__ == "__main__":
    main()