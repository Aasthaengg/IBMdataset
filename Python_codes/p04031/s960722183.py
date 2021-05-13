n = int(input())
l = list(map(int,input().split()))
m = round(sum(l)/len(l))
ans = 0
for i in range(len(l)):
  ans += (m - l[i])**2

print(ans)