N=int(input())
A=[int(input()) for i in range(N)]
A=A+[0]
ans=0
d=0
for i in A:
  if i!=0:
    d+=i
  else:
    ans+=d//2
    d=0
print(ans)