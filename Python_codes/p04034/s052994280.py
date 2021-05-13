N,M = map(int,input().split())

dp = [False]*N
dp[0] = True
cnt = [1]*N

for _ in range(M):
    x,y = map(lambda x:int(x)-1,input().split())
    dp[y] = dp[y] or dp[x]
    cnt[y] += 1
    cnt[x] -= 1
    if cnt[x] == 0:
        dp[x] = False

print(sum(dp))
