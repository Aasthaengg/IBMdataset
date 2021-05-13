n,m=map(int,input().split())
l=[]
for _ in range(m):
    l.append(list(map(int,input().split())))
a=[0]*(n+1)
a[1]=1
c=[1]*(n+1)
for i in range(m):
    c[l[i][0]]-=1
    c[l[i][1]]+=1
    if a[l[i][0]]:
        a[l[i][1]]=1
    if c[l[i][0]]==0:
        a[l[i][0]]=0
print(a.count(1))