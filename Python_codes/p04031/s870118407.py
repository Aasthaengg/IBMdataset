n=int(input())
l=list(map(int,input().split()))
k=[]
a=min(l)
b=max(l)
for i in range(a,b+1):
  c=0
  for j in range(n):
    c=c+(l[j]-i)**2
  k.append(c)
print(min(k))