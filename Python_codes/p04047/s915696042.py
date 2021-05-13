n = int(input())
l = [int(i) for i in input().split()]
l.sort()

ans = 0
for i in range(1, len(l), 2):
  ans += min(l[i-1], l[i])

print(ans)