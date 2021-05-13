n=int(input())
l=list(map(int,input().split()))
l.sort()
ans=0
for _ in range(n):
  ans+=l[2*_]
print(ans)