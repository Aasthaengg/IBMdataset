# coding: utf-8
# Your code here!
N,A=map(int,input().split())

X=list(map(int,input().split()))

dp=[[0]*2501 for i in range(50)]

for x in X:
    for i in range(49)[::-1]:
        for index,item in enumerate(dp[i]):
            if item!=0:
                dp[i+1][index+x]+=dp[i][index]
    dp[0][x]+=1

ans=0
for i in range(50):
    ans+=dp[i][A*(i+1)]

print(ans)
