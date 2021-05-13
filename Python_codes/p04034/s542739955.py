import numpy as np

N,M=map(int,input().split())
length=np.ones(N+1)
aka=np.ones(N+1)
aka[1]=-1

for _ in range(M):
  x,y=map(int,input().split())
  if aka[x]==-1:
    aka[y]=-1
  if length[x]-1==0:
    aka[x]=1
  length[x]-=1
  length[y]+=1

print(len(aka[aka<0]))