n = int(input())
a_lst = list(map(int, input().split()))
max_ = max(a_lst)
min_ = min(a_lst)
res = 0
for num in range(min_, max_+1):
  cost = 0
  for a in a_lst:
    cost += (a - num) ** 2
  if res != 0:
    res = min(res, cost)
  else:
    res = cost
print(res)