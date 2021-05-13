n = int(input())
l = sorted(list(map(int, input().split())))
ans = 0
for i in range(0,n*2,2):
  ans += min(l[i],l[i+1])
print(ans)