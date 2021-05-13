n,m=map(int,input().split())
a=[[int(i) for i in input().split()] for i in range(m)]

possibility=[False]*n
possibility[0]=True
count=[1]*n

for x,y in a:
    if possibility[x-1]==True and count[x-1]>1:
        possibility[y-1]=True
    elif possibility[x-1]==True and count[x-1]==1:
        possibility[x-1]=False
        possibility[y-1]=True
    count[x-1]-=1
    count[y-1]+=1

print(possibility.count(True))
