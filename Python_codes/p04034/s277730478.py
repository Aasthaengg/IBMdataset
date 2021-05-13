
n,m = list(map(int, input().split()))
manu = []

for i in range(m):
    manu.append(list(map(int, input().split())))

num = [1 for i in range(n+1)]
poss = [0 for i in range(n+1)]
poss[1] = 1

for i in range(m):
    a,b = manu[i][0],manu[i][1]
    if(poss[a]==1):
        poss[b]=1
    num[a]-=1
    num[b]+=1
    if(num[a]==0):
        poss[a]=0

print(sum(poss))
