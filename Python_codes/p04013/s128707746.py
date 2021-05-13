N,A=map(int,input().split())
x=list(map(int,input().split()))
ans=0
y=[0]*(len(x))
for k in range(len(x)):
    y[k]=x[k]-A
minus=0
plus=0
for k in range(N):
    if y[k]<0:
        minus-=y[k]
    if y[k]>0:
        plus+=y[k]
total=minus+plus+1
ans=[[0 for i in range(N)]for j in range(total)]
ans[y[0]+minus][0]=1
ans[minus][0]=ans[minus][0]+1
for j in range(N-1):
    for t in range(total):
        if 0<=t-y[j+1]<total:
            ans[t][j+1] =ans[t][j]+ans[t-y[j+1]][j]
        else:
            ans[t][j+1] =ans[t][j]
print(ans[minus][N-1]-1)