n,a=map(int,input().split())
lists=list(map(int,input().split()))
 
for i in range(n):
    lists[i]-=a
answer=0
dp=[[0 for i in range(5001)] for _ in range(51)]
#dp[i][j]で0からi枚目まで好きなように選択してそのそうわがｊ-2500となるような撮り方の総数
#最終的に求めるのはdp[i][0]である
 
for i in range(n+1):
    for j in range(4951):
        if i>=1 and j>=lists[i-1]:
            dp[i][j]=dp[i-1][j-lists[i-1]]+dp[i-1][j]
        if i>=1 and j<lists[i-1]:
            dp[i][j]=dp[i-1][j]
        else:
            if j==2500 and i==0:
                dp[i][j]=1
            elif j!=2500 and i==0:
                dp[i][j]=0
print(dp[n][2500]-1)  