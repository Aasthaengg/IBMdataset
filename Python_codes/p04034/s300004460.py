N,M=map(int,input().split())
arr=[[0,1,0] for _ in range(N)]
arr[0]=[1,1,1]
for i in range(M):
  a,b=map(int,input().split())
  arr[a-1][1]-=1
  arr[b-1][1]+=1
  if arr[a-1][0]==1:
    arr[b-1][0]=1
  if arr[a-1][2]==1:
    arr[a-1][2],arr[b-1][2]=0,1
  if arr[a-1][1]==0:
    arr[a-1][0]=0
ans=0
for i in range(N):
  if arr[i][0]==1 and arr[i][1]!=0:
    ans+=1
print(ans)