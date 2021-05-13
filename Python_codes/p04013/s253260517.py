n,k = map(int,input().split())
a = list(map(int,input().split()))
a = [a[i]-k for i in range(n)]
DP = [[0 for i in range(5100)] for j in range(52)]
for i in range(52):
    DP[i][2530] = 1
for i in range(1,n+1):
    for j in range(5050):
        DP[i][j] = DP[i-1][j] + DP[i-1][j-a[i-1]]
print(DP[n][2530]-1)