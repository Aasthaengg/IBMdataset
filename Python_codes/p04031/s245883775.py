n = int(input())
a = list(map(int, input().split()))

x = sum(a) / n
y = sum(a) // n
if x == y:
   cand = [y]
else:
   cand = [y, y+1]

cost = 10**18
for ave in cand:
   c = 0
   for i in range(n):
      c += (a[i]-ave)**2
   cost = min(cost, c)

print(cost)
