n,m=map(int,input().split())
ans=[0 for _ in range(n+1)]
cnt=[1 for _ in range(n+1)]
ans[1]=1
for i in range(m):
  a,b=map(int,input().split())
  if ans[a]==1:
    ans[b]=1
    if cnt[a]==1:
      ans[a]=0
  cnt[a]-=1
  cnt[b]+=1
print(sum(ans))