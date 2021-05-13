N = int(input())
A = list(map(int, input().split()))
ans = float('inf')

for target in range(-100, 101):
  cost = 0
  for j, a in enumerate(A):
    cost += (target - a)**2
  ans = min(ans, cost)

print(ans)