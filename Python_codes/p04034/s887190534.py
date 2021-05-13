n, m = map(int, input().split())
rednow = [-1, 1] + [0 for i in range(n-1)] # maybe there's red ball
balnum = [-1] + [1 for i in range(n)] # the number of ball, each box
order = []
for i in range(m):
  order.append(list(map(int, input().split()))) 

for q in order:
  if rednow[q[0]] == 1:
    rednow[q[1]] = 1
    if balnum[q[0]] == 1:
      rednow[q[0]] = 0
  balnum[q[0]] -= 1
  balnum[q[1]] += 1

print(rednow.count(1))
