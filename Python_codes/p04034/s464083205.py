n,m=map(int,input().split())
l=[1]+[0]*(n+1)
a=[1]*n
for i in range(m):
 x,y=map(int,input().split())
 if l[x-1]:l[y-1]=1
 a[x-1]-=1;a[y-1]+=1
 if not a[x-1]:l[x-1]=0
print(l.count(1))