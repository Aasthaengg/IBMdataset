n,l=map(int,input().split())
S=list(input() for _ in range(n))
S.sort()
ans=""
for i in range(n):
  ans+=S[i]
print(ans)