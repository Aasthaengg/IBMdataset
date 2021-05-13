from sys import stdin
def main():
    #入力
    readline=stdin.readline
    con=2500
    n,a=map(int,readline().split())
    x=list(map(int,readline().split()))

    dp=[[[0]*(n+1) for _ in range(con+1)] for _ in range(n+1)]
    dp[0][0][0]=1
    for i in range(n):
        for k in range(n):
            for j in range(con+1-50):
                #i枚目を選ぶ
                dp[i+1][j+x[i]][k+1]+=dp[i][j][k]

                #i枚目を選ばない
                dp[i+1][j][k]+=dp[i][j][k]

    ans=0
    for k in range(1,n+1):
        ans+=dp[n][k*a][k]
    print(ans)

if __name__=="__main__":
    main()