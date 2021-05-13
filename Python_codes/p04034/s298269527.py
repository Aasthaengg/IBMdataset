N,M=map(int,input().split())
X=[0]*(N+1)
X[1]=1
Y=[1]*(N+1)
a,b=0,0
for i in range(M):
  a,b=map(int,input().split())
  X[b]|=X[a]
  Y[b]+=1
  Y[a]-=1
  if Y[a]==0:
    X[a]=0
print(sum(X))