n,l = map(int,input().split())
s = []
for i in range(n):
  s.append(input())
sort_s = sorted(s)
ans = ''
for i in sort_s:
  ans += i
print(ans)