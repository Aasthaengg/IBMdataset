n = int(input())
l = sorted(list(map(int,input().split())),reverse = True)

ans = 0
for i in range(n):
  ans += l[i*2+1]
print(ans)
