N,A = map(int,input().split())
x = list(map(int,input().split()))

for i in range(N):
    x[i] -= A

dp = [0]*5000###-2500~2499,idx=2500が0に対応
dp[2500] = 1

for i in range(N):
    pre = dp[:]
    for j in range(max(0,-x[i]),min(4999,4999-x[i])):
        dp[j+x[i]] += pre[j]
    #print(pre[2490:2510])
    #print(dp[2490:2510])

#print(x)
print(dp[2500]-1)