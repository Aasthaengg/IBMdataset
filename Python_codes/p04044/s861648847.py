n,l =map(int,input().split())
ss = [input() for _ in range(n)]
s =sorted(ss)
ans =""
for i in s:
  ans += i
print(ans)