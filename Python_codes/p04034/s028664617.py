import sys

N,M=map(int,input().split())
ope=[]
for i in range(M):
    ope.append(tuple(map(int,input().split())))

state=[1]*N
red=[0]*N
red[0]=1
for i in range(M):
    x,y=ope[i]
    if red[x-1]:
        if state[x-1]>1:
            red[x-1]=1
            red[y-1]=1
        else:
            red[x-1]=0
            red[y-1]=1
    state[x-1]-=1
    state[y-1]+=1

print(sum(red))
