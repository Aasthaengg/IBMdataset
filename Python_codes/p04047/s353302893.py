N = int(input())
x = list(map(int,input().split()))

x = sorted(x,reverse = True)

ans = 0
for i in range(len(x)):
  if i % 2 == 0:
    ans += min(x[i],x[i+1])

print(ans)
