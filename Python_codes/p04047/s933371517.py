n=int(input())
a=list(map(int,input().split()))
ans=0
b=[]
for k in range(2*n):
 for i in range(2*n):
  if a[i]==min(a):
    b.append(a[i])
    a[i]=101
for s in range(n):
  ans+=b[2*s]
print(ans)