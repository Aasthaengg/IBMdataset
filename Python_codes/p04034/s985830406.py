n,m=map(int,input().split())
s=set([1])
b=[1]*(n+1)
for i in range(m):
  x,y=map(int,input().split())
  b[x]-=1
  b[y]+=1
  if x in s:
    s.add(y)
    if b[x]==0:
      s.remove(x)
print(len(s))